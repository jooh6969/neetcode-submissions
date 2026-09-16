class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (right + left) // 2
            if nums[mid] < nums[mid + 1] and nums[mid] < nums[mid - 1]:
                return nums[mid]
            # if left > mid and right, and mid isn't the lowest, then my elem is to the left
            # else, search on the side with the lower element
            if nums[left] > nums[mid] and nums[left] > nums[right]:
                right = mid - 1
            elif nums[left] > nums[right]:
                left = mid + 1
            else:
                right = mid - 1
        return nums[left]