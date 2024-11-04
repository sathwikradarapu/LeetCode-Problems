class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        hash_map1={}
        hash_map2={}
        s=s.split()
        if len(pattern)==len(s):
            for i in range(len(pattern)):
                v1=pattern[i]
                v2=s[i]
                if v1 not in hash_map1 and v2 not in hash_map2:
                    hash_map1[v1]=v2
                    hash_map2[v2]=v1
                if v1 in hash_map1 and hash_map1[v1]!=v2:
                    return False
                if v2 in hash_map2 and hash_map2[v2]!=v1:
                    return False
            return True
        else:
            return False