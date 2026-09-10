class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        m = len(t)
        if n < m:
            return ""
        t_ctr = Counter(t)
        s_ctr = Counter()
        need = len(t_ctr)
        have = 0
        left = 0
        best_left = 0
        best_len = float('inf')
        for right in range(n):
            c = s[right]
            s_ctr[c] += 1
            if c in t_ctr and s_ctr[c] == t_ctr[c]:
                have += 1
            while have == need:
                if right - left + 1 < best_len:
                    best_len = right - left + 1
                    best_left = left
                c = s[left]
                s_ctr[c] -= 1
                if c in t_ctr and s_ctr[c] < t_ctr[c]:
                    have -= 1
                left += 1
        if best_len == float('inf'):
            return ""
        return s[best_left: best_left + best_len]




