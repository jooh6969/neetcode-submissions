class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        ans = s[0]
        best_len = -float("inf")
        for i in range(n):
            # odd length palindromes
            left = i - 1
            right = i + 1
            while left >= 0 and right < n and s[left] == s[right]:
                if best_len < right - left + 1:
                    best_len = right - left + 1
                    ans = s[left:right + 1]
                left -= 1
                right += 1
            # even length palindromes
            left = i
            right = i + 1
            while left >= 0 and right < n and s[left] ==  s[right]:
                if best_len < right - left + 1:
                    best_len = right - left + 1
                    ans = s[left: right + 1]
                left -= 1
                right += 1
        return ans

