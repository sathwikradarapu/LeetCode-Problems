from typing import List

class Solution:
    def captureForts(self, forts: List[int]) -> int:
        ans=0
        last=-1
        for i in range(len(forts)):
            if forts[i]==1 or forts[i]==-1:
                if last!=-1 and forts[i]!=forts[last]:
                    ans=max(ans,i-last-1)
                last=i
        return ans