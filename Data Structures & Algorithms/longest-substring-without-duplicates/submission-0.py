class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = {}
        maxlength = 0
        left = 0

        for right in range (len(s)):
            char = s[right]
            if char in window:
                left = max(left, window[char]+1)
            window[char] = right
            maxlength = max(maxlength, right - left + 1)
        return maxlength
        