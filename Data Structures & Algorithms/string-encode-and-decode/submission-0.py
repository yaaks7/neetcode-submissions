class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for s in strs:
            # Number of character in the word, delimiter, word
            ans += str(len(s)) + "#" + s
        return ans


    def decode(self, s: str) -> List[str]:
        ans, i = [], 0

        while i < len(s):
            j=i
            while s[j] != "#": #find the delimiter
                j+=1
            length = int(s[i:j]) #Get the number of character 
            ans.append(s[j+1 : j+1+length])
            i = j + 1 + length
        return ans
        


