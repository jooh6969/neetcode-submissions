class TimeMap:

    def __init__(self):
        self.timeMap = {}
        # elements are going to be of the following form
        # (key, [(value, timestamp)])
        # we search based on the timestamp

    def set(self, key: str, value: str, timestamp: int) -> None:
        # the timestamps of this function are strictly increasing
        self.timeMap.setdefault(key, []).append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        val = self.timeMap.get(key, "")
        # if my first entry already is > given timestamp, won't find
        if val == "" or val[0][1] > timestamp:
            return ""
        left = 0
        right = len(val) - 1
        while left < right:
            mid = (left + right + 1) // 2
            elem = val[mid]
            if elem[1] > timestamp: # not the right element
                right = mid - 1
            else: # could be the answer
                left = mid # when i do left = mid, the left and right pointer may not change, so i need my mid to be (left + right + 1) // 2 instead
        return val[left][0]
        
        
