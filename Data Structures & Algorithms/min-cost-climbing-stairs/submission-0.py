class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memo = [-1] * n
        memo[0] = cost[0]
        memo[1] = cost[1]
        # memo[n] is the path cost up to this point, including this step
        for i in range(2, n):
            memo[i] = cost[i] + min(memo[i - 1], memo[i - 2])
        return min(memo[n - 1], memo[n - 2])

        
        