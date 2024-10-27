class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n=len(blocks)
        ans=float("inf")
        for i in range(n):
            for j in range(i+1,n+1):
                temp=blocks[i:j]
                if len(temp)==k:
                    count=temp.count('W')
                    ans=min(ans,count)
        return ans
            