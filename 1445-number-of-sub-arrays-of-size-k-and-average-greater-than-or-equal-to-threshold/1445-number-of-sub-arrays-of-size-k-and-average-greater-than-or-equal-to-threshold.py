class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l=0
        n=len(arr)
        temp=0
        count=0
        for r in range(n):
            temp+=arr[r]
            if r-l==k:
                temp-=arr[l]
                l+=1
            if r-l+1==k:
                if temp/k>=threshold:
                    count+=1
        return count