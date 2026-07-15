class Solution:
    def reverseBits(self, n: int) -> int:
        # idea is that bit i should be bit (31 - i)
        ans = 0
        for i in range(32):
            curr_bit = n & 1
            n >>= 1
            ans |= curr_bit << (31 - i)
        return ans