class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)
        if n > m:
            return False
        left = 0
        right = n - 1
        seen = Counter(s1)
        current = Counter(s2[left:right + 1])
        while right < m - 1:
            if seen == current:
                return True
            current[s2[left]] -= 1
            left += 1
            right += 1
            current[s2[right]] += 1
            # ill miss the last iteration here, so just return the check
        return current == seen

        