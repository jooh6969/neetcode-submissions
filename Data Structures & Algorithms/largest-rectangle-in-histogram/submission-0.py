class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # each stack entry is (idx, height)
        stack = []
        max_area = 0
        for i, height in enumerate(heights):
            start = i
            while stack and stack[-1][1] > height: # encountered a shorter bar
                p_idx, p_height = stack.pop() # bar can't extend, so we compute height
                max_area = max(max_area, p_height * (i - p_idx))
                start = p_idx # this popped index can include a rectangle of this lower height
            stack.append((start, height))
        # if we don't encounter a shorter rectangle, everyth to the right can be used
        # so we take (len - idx) * height to get the area
        for idx, height in stack:
            max_area = max(max_area, height * (len(heights) - idx))
        return max_area

