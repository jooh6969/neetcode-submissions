class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        # a := distance from [0] to cycle entrance
        # b := distance from cycle entrance to the point where slow and fast meets
        # c := distance of the cycle
        # for any distance d travelled by slow, since fast is twice as fast, the diff between
        # them is exactly d
        # since they meet in the cycle, this difference must be some multiple of the cycle length
        # as the fast ptr mustve went rounds around the cycle to catch slow
        # d = kc
        # at the same time, d = a + b + mc
        # we have (k-m) c = a + b
        # since a + b is a multiple of c, fast will be at distance b from cycle entrance
        # i can advance both pointers forward a times and they will meet at the cycle entrance
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
