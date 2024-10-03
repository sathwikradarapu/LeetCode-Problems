class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n=len(arr)
        rmax=-1
        for i in range(n-1,-1,-1):
            temp=arr[i]
            arr[i]=rmax
            rmax=max(temp,arr[i])
        return arr