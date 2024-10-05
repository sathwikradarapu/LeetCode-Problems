class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hash_map={}
        if len(s)==len(t):
            for i in range(len(s)):
                if s[i] not in hash_map:
                    if t[i] not in hash_map.values():
                        hash_map[s[i]]=t[i]
                    else:
                        return False
                else:
                    if t[i]!=hash_map[s[i]]:
                        return False
        return True