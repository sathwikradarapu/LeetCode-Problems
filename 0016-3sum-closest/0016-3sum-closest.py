class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n=len(nums)
        i=0
        ans=float("inf")
        while i<n:
            j=i+1
            k=n-1
            while j<k:
                a=nums[i]
                b=nums[j]
                c=nums[k]
                d=a+b+c
                e=abs(target-d)
                f=abs(target-ans)
                if e<f:
                    ans=d
                if d<target:
                    j+=1
                elif d>target:
                    k-=1
                else:
                    return d
            i+=1
        return ans