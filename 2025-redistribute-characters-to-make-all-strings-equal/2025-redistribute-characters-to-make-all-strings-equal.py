class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        dici={}
        for i in words:
            for j in i:
                if j not in dici:
                    dici[j]=1
                else:
                    dici[j]+=1
        for i in dici:
            if dici[i]%len(words)!=0:
                return False
        return True