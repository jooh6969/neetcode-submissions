class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix) # across rows
        n = len(matrix[0]) # across cols
        top = 0
        bottom = m - 1
        while top < bottom:
            mid = (bottom + top) // 2
            if matrix[mid][n - 1] == target:
                return True
            if matrix[mid][n - 1] < target:
                top = mid + 1
            else:
                bottom = mid # can't eliminate this row
        # my loop above ends with top == bottom, meaning this is the row
        # i should be checking
        mid = top
        left = 0
        right = n - 1
        while left <= right:
            middle = (right + left) // 2
            if matrix[mid][middle] == target:
                return True
            if matrix[mid][middle] < target:
                left = middle + 1
            else:
                right = middle - 1
        return False