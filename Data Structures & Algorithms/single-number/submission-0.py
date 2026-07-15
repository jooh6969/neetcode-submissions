class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # 0 XOR n = n, and n XOR n = 0, so the only digit that isn't duplicated
        # will be the value that's stored in value
        value = 0
        for num in nums:
            value ^= num
        return value