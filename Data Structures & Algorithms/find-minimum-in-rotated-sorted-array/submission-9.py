class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (right + left) // 2
            if nums[mid] > nums[right]: # mid can't be minimum, and min must be on the right side
                left = mid + 1
            else:
                right = mid
        return nums[left]