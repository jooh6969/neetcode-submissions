class Solution:
    def rob(self, nums: List[int]) -> int:
        # at each house, I either rob it and take 2 steps, or I don't rob it
        # and take 1 step forward
        n = len(nums)
        def helper(idx, nums, dp):
            if idx >= n:
                return 0
            if dp[idx] != -1:
                return dp[idx]
            dp[idx] = max(nums[idx] + helper(idx + 2, nums, dp), helper(idx + 1, nums, dp))
            return dp[idx]

        dp = [-1] * n
        # with only 1 house, i should rob it
        return helper(0, nums, dp)
        


        
