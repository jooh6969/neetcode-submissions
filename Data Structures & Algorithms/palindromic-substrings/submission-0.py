class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        n = len(s)
        for i in range(n):
            # odd length palindromes
            count += 1 # length 1 substrings are also considered palindromes
            left = i - 1
            right = i + 1
            while left >= 0 and right < n and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            # even length palindromes
            left = i
            right = i + 1
            while left >= 0 and right < n and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
        return count