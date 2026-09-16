class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (right + left) // 2
            if nums[mid] < nums[mid + 1] and nums[mid] < nums[mid - 1]:
                return nums[mid]
            # if mid > ends, move to the smaller end
            # else move to the smaller end
            if nums[left] > nums[mid] and nums[left] > nums[right]:
                right = mid - 1
            elif nums[left] > nums[right]:
                left = mid + 1
            else:
                right = mid - 1
        return nums[left]