class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = [[]]
        # append modifies ans, but returns none, so i can't do the append
        # and the return on the same line
        if len(strs) <= 1:
            ans[0].append(strs[0])
            return ans
        letter_group = []
        first_letters = Counter(strs[0])
        letter_group.append(first_letters)
        ans[0].append(strs[0])
        for s in strs[1:]:
            found = False
            curr_letters = Counter(s)
            for i, letters in enumerate(letter_group):
                tmp = i
                # if found in group of letters, append to this position
                if curr_letters == letters:
                    ans[i].append(s)
                    found = True
                    break
            # if not found, make a new dictionary group, 
            # append the answer to the next pos
            if not found:
                tmp += 1
                ans.append([])
                letter_group.append(curr_letters)
                ans[tmp].append(s)
        return ans
