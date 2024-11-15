class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l=0
        ans=0
        dici={}
        for r in range(len(fruits)):
            val=fruits[r]
            if val in dici:
                dici[val]+=1
            else:
                dici[val]=1
            while len(dici)>2:
                val2=fruits[l]
                dici[val2]-=1
                if dici[val2]==0:
                    dici.pop(val2)
                l+=1
            ans=max(ans,r-l+1)
        return ans
