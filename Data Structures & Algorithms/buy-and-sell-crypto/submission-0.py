class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        MINIMUM = -float('inf')
        # let dp[i] represent the max profit obtainable if i bought the
        # coin on day i
        dp = [MINIMUM] * n
        for i in range(n):
            for j in range(i + 1, n):
                dp[i] = max(dp[i], prices[j] - prices[i])
                print(dp[i])
        return max(max(dp), 0)
