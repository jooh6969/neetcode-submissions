class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        ans = 0
        for num in seen:
            if num - 1 in seen:
                continue
            tmp = 1
            start = num + 1
            while start in seen:
                tmp += 1
                start += 1
            ans = max(ans, tmp)
        return ans

