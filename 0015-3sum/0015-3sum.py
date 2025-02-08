class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        a=set()
        b=[]
        i=0
        while i<n and nums[i]<=0:
            j=i+1
            k=n-1
            while j<n and j<k and k>0:
                c=nums[i]
                d=nums[j]
                e=nums[k]
                f=0-c
                if d+e==f:
                    g=[c,d,e]
                    g.sort()
                    a.add(tuple(g))
                    j+=1
                    k-=1
                elif d+e<f:
                    j+=1
                else:
                    k-=1
            i+=1
        for i in a:
            i=list(i)
            b.append(i)
        return b