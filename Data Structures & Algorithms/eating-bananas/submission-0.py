class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minimum = 1
        maximum = max(piles)
        while minimum < maximum:
            mid = (maximum + minimum) // 2
            time = 0
            for pile in piles:
                time += math.ceil(pile / mid)
            if time > h:
                minimum = mid + 1
            else:
                maximum = mid
        return minimum