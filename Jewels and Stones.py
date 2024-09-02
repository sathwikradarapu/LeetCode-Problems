class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count=0
        for i in jewels:
            for j in stones:
                if j==i:
                    count+=1
        return count
