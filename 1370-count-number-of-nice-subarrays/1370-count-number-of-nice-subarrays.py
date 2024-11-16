class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def atMostK(arr,k):
            l=0
            temp=0
            n=len(arr)
            ans=float("-inf")
            count=0
            for r in range(n):
                if arr[r]%2==1:
                    temp+=1
                while temp>k:
                    if arr[l]%2==1:
                        temp-=1
                    l+=1
                ans=max(ans,r-l+1)
                count+=r-l+1
            return count
        a=atMostK(nums,k)
        b=atMostK(nums,k-1)
        c=a-b
        return c