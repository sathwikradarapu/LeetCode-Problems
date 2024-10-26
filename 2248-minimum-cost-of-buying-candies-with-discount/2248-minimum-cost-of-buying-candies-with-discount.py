class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost=sorted(cost,reverse=True)
        took=0
        ans=0
        for i in cost:
            if took==2:
                took=0
            else:
                ans+=i
                took+=1
        return ans
                

