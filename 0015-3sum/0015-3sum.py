class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        i=0
        ans=set()
        nums=sorted(nums)
        res=[]
        while i<n and nums[i]<=0:
            j=i+1
            k=n-1
            while j<k and j<n and k>=0:
                n1=nums[i]
                n2=nums[j]
                n3=nums[k]
                target=0-n1
                if n2+n3==target:
                    n4=(n1,n2,n3)
                    n4=tuple(sorted(n4))
                    ans.add(n4)
                    j+=1
                    k-=1
                elif n2+n3<target:
                    j+=1
                elif n2+n3>target:
                    k-=1
            i+=1
        for i in ans:
            res.append(list(i))
        return res
