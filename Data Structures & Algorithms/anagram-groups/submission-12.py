class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = [[]]
        if len(strs) <= 1:
            return [strs]
        dictionaries = {}
        first = tuple(sorted(Counter(strs[0]).items()))
        dictionaries[first] = 0
        position = 1
        ans[0].append(strs[0])
        for s in strs[1:]:
            curr_dict = tuple(sorted(Counter(s).items()))
            if curr_dict in dictionaries:
                idx = dictionaries[curr_dict]
                ans[idx].append(s)
            else:
                dictionaries[curr_dict] = position
                position += 1
                ans.append([s])
        return ans

