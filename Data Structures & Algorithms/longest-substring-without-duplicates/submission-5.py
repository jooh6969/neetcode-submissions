class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        n = len(s)
        right = left
        seen = set()
        ans = 0
        while right < n:
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            ans = max(ans, right - left + 1) 
            right += 1       
        return ans
            
