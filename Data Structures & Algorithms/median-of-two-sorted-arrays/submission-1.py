class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # x is the number of elements i pick out from the bigger array
        # B = [1,2,3,4,5], A = [1,2,3,4,5,6,7,8]
        # if x == 5, i need 2 from A
        # so i pick [1,2] from A, [1,2,3,4,5] from B
        m = len(nums1)
        n = len(nums2)
        if m < n:
            A, B = nums1, nums2
        else:
            A, B = nums2, nums1
        # A will always be the smaller array
        medianPosition = (n + m + 1) // 2
        left = 0
        right = len(A)
        while left <= right:
            # take x as the count of elements in A, y as the count of elements in B
            # x is how many i take from A
            # y is how many i take from B
            x = (left + right) // 2
            y = medianPosition - x
            Aleft = A[x - 1] if x > 0 else float('-inf')
            Aright = A[x] if x < len(A) else float('inf')
            Bleft = B[y - 1] if y > 0 else float('-inf')
            Bright = B[y] if y < len(B) else float('inf')
            if Aleft <= Bright and Bleft <= Aright:
                # valid partition
                if (m + n) % 2 == 1:
                    # odd count
                    return max(Aleft, Bleft)
                else:
                    # even count, since medianPosition was floored
                    # i need 1 from left and 1 from right
                    return (max(Aleft, Bleft) + min(Aright, Bright)) /2
            elif Aleft > Bright:
                # took too many from A
                right = x - 1
            else:
                left = x + 1
                



