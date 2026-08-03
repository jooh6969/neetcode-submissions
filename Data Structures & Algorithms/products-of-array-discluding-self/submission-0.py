class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pdt = 1
        zeros = [] # index of the 0's
        n = len(nums)
        for i, num in enumerate(nums):
            if num == 0:
                zeros.append(i)
            else:
                pdt *= num 
                # i keep the product for non-zeros
        if len(zeros) > 1:
            # with 2 0's the product is 0 everywhere
            return [0] * n
        elif len(zeros) == 1:
            nums = [0] * n
            nums[zeros[0]] = pdt
        else:
            for i in range(n):
                nums[i] = pdt // nums[i]
        return nums

        