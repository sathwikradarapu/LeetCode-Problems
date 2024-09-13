class Solution:
    def scoreOfString(self, s: str) -> int:
        temp=0
        for i in range(len(s)-1):
            temp+=abs(ord(s[i])-ord(s[i+1]))
        return temp