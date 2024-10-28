from typing import List

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr=sorted(arr)
        ans=float("inf")
        temp=[]
        for i in range(1,len(arr)):
            diff=arr[i]-arr[i-1]
            if diff<ans:
                ans=diff
                temp=[[arr[i-1],arr[i]]]
            elif diff==ans:
                temp.append([arr[i-1],arr[i]])
        return temp