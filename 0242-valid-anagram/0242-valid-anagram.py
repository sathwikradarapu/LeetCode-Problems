class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dici1=dict()
        dici2=dict()
        for i in s:
            if i not in dici1:
                dici1[i]=1
            else:
                dici1[i]+=1
        for j in t:
            if j not in dici2:
                dici2[j]=1
            else:
                dici2[j]+=1
        return(dici1==dici2)