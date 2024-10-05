class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        hash_map={}
        for i in stones:
            if i in jewels:
                if i in hash_map:
                    hash_map[i]+=1
                else:
                    hash_map[i]=1
        return sum(hash_map.values())
        