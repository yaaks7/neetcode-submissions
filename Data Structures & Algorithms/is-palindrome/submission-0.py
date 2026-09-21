class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower().replace(" ","")
        s=''.join(filter(str.isalnum, s))
        
        left, right = 0, len(s) - 1

        while  left < right:
            if s[left] == s[right]:
                left +=1
                right -=1
            
            else : 
                return False
        return True
        
        

        