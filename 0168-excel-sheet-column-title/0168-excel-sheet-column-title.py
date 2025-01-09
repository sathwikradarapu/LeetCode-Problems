class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans=""
        while columnNumber>0:
            offset=(columnNumber-1)%26
            ans+=chr(ord('A')+offset)
            columnNumber=(columnNumber-1)//26
        return ans[::-1]