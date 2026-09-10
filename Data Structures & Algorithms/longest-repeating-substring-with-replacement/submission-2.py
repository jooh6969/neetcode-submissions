class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # as i slide my pointer from left to right, i consider #char to replace
        # take right - left + 1 - #most freq
        left = 0
        right = left
        count = {}
        max_freq = 0
        ans = 0
        while right < len(s):
            c = s[right]
            count[c] = count.get(c, 0) + 1
            max_freq = max(max_freq, count[c])
            while (right - left + 1) - max_freq > k:
                d = s[left]
                count[d] -= 1
                left += 1
            ans = max(ans, right - left + 1)
            right += 1
        return ans
