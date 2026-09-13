class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combined = []
        for i in range(len(position)):
            combined.append((position[i], speed[i]))
        combined.sort(key = lambda x: -x[0])
        ref_time = (target - combined[0][0]) / combined[0][1] # how long the furthest car takes
        fleets = 1 # combine the rest of the cars
        stack = []
        for combination in combined[1:]:
            position = combination[0]
            speed = combination[1]
            time_taken = (target - position) / speed
            if time_taken <= ref_time:
                continue
            else:
                fleets += 1
                ref_time = time_taken
        return fleets


