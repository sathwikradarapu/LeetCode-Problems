class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        t_hash={}
        for i in t:
            if i in t_hash:
                t_hash[i]+=1
            else:
                t_hash[i]=1
        for i in s:
            if i in t_hash:
                t_hash[i]-=1
            else:
                return False
        for i in t_hash:
            if t_hash[i]!=0:
                return False
        return True