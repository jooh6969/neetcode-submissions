class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        for i in range(1, n + 1):
            count = 0
            for j in range(10):
                if 1 << j & i:
                    count += 1
            ans[i] = count
        return ans
        