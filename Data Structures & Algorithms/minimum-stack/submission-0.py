class MinStack:
    # each element would contain the smallest element above, self included
    # as well as itself
    # (curr_element, smallest_thus_far)
    def __init__(self):
        self.minStack = []

    def push(self, val: int) -> None:
        if not self.minStack:
            self.minStack.append((val, val))
        else:
            prev = self.minStack[-1][1]
            minimum = min(prev, val)
            self.minStack.append((val, minimum))
        
    def pop(self) -> None:
        val = self.minStack.pop()

    def top(self) -> int:
        return self.minStack[-1][0]

    def getMin(self) -> int:
        return self.minStack[-1][1]
