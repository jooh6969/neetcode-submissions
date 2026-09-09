class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_area = 0
        while left < right:
            base = right - left
            height = min(heights[left], heights[right])
            max_area = max(max_area, base * height)
            if heights[left] >= heights[right]:
                right -= 1
            else:
                left += 1
        return max_area
