class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        hashmap_s,hashmap_t={},{}
        res=""
        for i in s:
            if i not in hashmap_s:
                hashmap_s[i]=1
            else:
                hashmap_s[i]+=1
        for i in t:
            if i not in hashmap_t:
                hashmap_t[i]=1
            else:
                hashmap_t[i]+=1
        for i in hashmap_t:
            if i not in hashmap_s or hashmap_s[i]!=hashmap_t[i]:
                res+=i
        return res