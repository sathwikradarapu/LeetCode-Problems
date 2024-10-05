class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hash_map1={}
        hash_map2={}
        for i in range(len(s)):
            v1=s[i]
            v2=t[i]
            if v1 not in hash_map1 and v2 not in hash_map2:
                hash_map1[v1]=v2
                hash_map2[v2]=v1
            if v1 in hash_map1 and hash_map1[v1]!=v2:
                return False
            if v2 in hash_map2 and hash_map2[v2]!=v1:
                return False
        return True