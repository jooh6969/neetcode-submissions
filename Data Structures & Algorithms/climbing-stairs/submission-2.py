class Solution:
    def climbStairs(self, n: int) -> int:
        # climbStairs(n) returns me the number of ways to climb to the top
        # of the stairs
        # recursion is climbStairs(n - 1), where I take 1 step from n - 1
        # + climbStairs(n - 2), where I take 2 steps from n - 2
        memo = [-1] * (n + 1)
        memo[0] = 1
        memo[1] = 1
        def memoClimbStairs(n, memo):
            if memo[n] != -1:
                return memo[n]
            memo[n] = memoClimbStairs(n - 1, memo) + memoClimbStairs(n - 2, memo)
            return memo[n]
        return memoClimbStairs(n, memo)
        