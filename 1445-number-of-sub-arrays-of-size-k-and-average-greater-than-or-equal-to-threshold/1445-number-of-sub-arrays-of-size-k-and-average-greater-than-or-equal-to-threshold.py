class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l=0
        n=len(arr)
        temp=[]
        count=0
        for r in range(n):
            temp.append(arr[r])
            if r-l==k:
                temp.pop(0)
                l+=1
            if r-l+1==k:
                if sum(temp)/k>=threshold:
                    count+=1
        return count