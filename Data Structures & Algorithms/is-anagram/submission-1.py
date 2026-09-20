class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        if len(s) != len(t):
            return False
        sCount =  Counter(s)
        tCount =  Counter(t)

        for char in sCount :
            if (char in tCount) and (sCount[char] == tCount[char]):
                continue
            else : 
                return False
        return True
        