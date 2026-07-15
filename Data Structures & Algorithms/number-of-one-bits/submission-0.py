class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        for i in range(31):
            mask = 1 << i
            if mask & n:
                count += 1
        return count
