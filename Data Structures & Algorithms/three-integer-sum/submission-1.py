class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # i start by sorting nums, then for each index, first i check if it's duplicated
        # if its duplicated, then i just skip it to prevent getting the same indices
        # then run a 2 pointer approach, since it's sorted, we change the pointer based on whether
        # the sum > or < the target
        nums.sort()
        ans = []
        n = len(nums)
        for i in range(n):
            # same element encountered past the first
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = n - 1
            while left < right:
                curr = nums[i] + nums[left] + nums[right]
                if curr == 0:
                    ans.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1 # we don't break after the first find, instead we continue
                    # change left and right while they're the same
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1 
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif curr > 0:
                    right -= 1
                else:
                    left += 1
        return ans