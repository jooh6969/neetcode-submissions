class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        # each elem is a tuple (temp, idx)
        stack = []
        for i, temp in enumerate(temperatures):
            if not stack:
                stack.append((temp, i))
                continue
            while stack and temp > stack[-1][0]:
                popped = stack.pop() # contains (temp, i)
                result[popped[1]] = i - popped[1]
            stack.append((temp, i))
        return result
        
