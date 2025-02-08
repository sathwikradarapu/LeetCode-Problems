class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l=0
        r=len(nums)-1
        res=[]
        while l<=r:
            a=nums[l]**2
            b=nums[r]**2
            if a>b:
               res.append(a)
               l+=1
            else:
                res.append(b)
                r-=1
        return res[::-1]