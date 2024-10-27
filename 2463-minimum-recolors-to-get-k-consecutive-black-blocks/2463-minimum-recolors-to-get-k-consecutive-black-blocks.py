class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l=0
        temp=""
        ans=float("inf")
        n=len(blocks)
        for r in range(n):
            temp+=blocks[r]
            if r-l==k:
                temp=temp[1:]
                l+=1
            if r-l+1==k:
                ans=min(ans,temp.count('W'))
        return ans
                    