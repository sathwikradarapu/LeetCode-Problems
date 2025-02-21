class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dici1={}
        dici2={}
        for i in ransomNote:
            if i not in dici1:
                dici1[i]=1
            else:
                dici1[i]+=1
        for i in magazine:
            if i in ransomNote:
                if i not in dici2:
                    dici2[i]=1
                else:
                    dici2[i]+=1
        if len(dici1)!=len(dici2):
            return False
        else:
            for i in dici1:
                a=dici1[i]
                b=dici2[i]
                if a>b:
                    return False
        return True