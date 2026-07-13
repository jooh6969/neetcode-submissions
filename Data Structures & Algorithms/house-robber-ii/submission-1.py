class Solution:
    def rob(self, nums: List[int]) -> int:
        # since the first and last houses are neighbours, i can only rob either
        # create 2 arrays, one without house 0
        # and 1 without house (n-1)
        # at each house, I either rob it and take 2 steps, or I don't rob it
        # and take 1 step forward
        n = len(nums)
        if n == 0:
            return 0
        elif n == 1:
            return nums[0] 
        def helper(idx, nums, dp):
            if idx >= n - 1: # this becomes n - 1 since i remove 1 hse
                return 0
            if dp[idx] != -1:
                return dp[idx]
            dp[idx] = max(nums[idx] + helper(idx + 2, nums, dp), helper(idx + 1, nums, dp))
            return dp[idx]

        dp_incl_first = [-1] * (n - 1)
        dp_excl_first = [-1] * (n - 1)
        nums_with_first = nums[0: n - 1]
        nums_without_first = nums[1: n]
        with_first = helper(0, nums_with_first, dp_incl_first)
        without_first = helper(0, nums_without_first, dp_excl_first)
        return max(with_first, without_first)
        


        
