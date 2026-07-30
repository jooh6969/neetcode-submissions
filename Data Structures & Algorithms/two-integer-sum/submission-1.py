class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        # store all of the values we encountered so far, and their idx
        for i, num in enumerate(nums):
            d[num] = i
        ans = []
        for i, num in enumerate(nums):
            diff = target - num
            if d.get(diff, -1) != -1 and i != d[diff]:
                if d[diff] < i:
                    ans += [d[diff], i]
                else:
                    ans += [i, d[diff]]
                return ans
        return ans
        