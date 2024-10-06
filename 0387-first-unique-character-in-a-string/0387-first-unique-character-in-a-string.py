class Solution:
    def firstUniqChar(self, s: str) -> int: 
        hash_map={}
        for i in range(len(s)):
            if s[i] in hash_map:
                hash_map[s[i]]+=1
            else:
                hash_map[s[i]]=1
        for i in hash_map:
            if hash_map[i]==1:
                return s.index(i)
        return -1
                