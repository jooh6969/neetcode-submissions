class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums) + 1):
            ans ^= i
        for num in nums:
            ans ^= num
        return ans
        # [a,b,c,d]
        # c missing
        # start with 0
        # 0 ^ (a ^ a) ^ (b ^ b) ^ (d ^ d) ^ c = c