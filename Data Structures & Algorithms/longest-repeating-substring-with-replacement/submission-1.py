class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        frequency = {}
        left = 0
        max_window = 0

        for right in range (len(s)):
            char = s[right]
            frequency[char] = frequency.get(char,0)+1
            window = right - left +1

            if (window - max(frequency.values())) > k :
                frequency[s[left]] -= 1
                left +=1
                window -=1
            max_window = max(max_window, window)
            
        return max_window