class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        l=len(mat)
        ans=0
        j=0
        k=l-1
        for i in range(l):
            arr=mat[i]
            if j!=k:
                ans+=arr[j]+arr[k]
            else:
                ans+=arr[j]
            j+=1
            k-=1
        return ans