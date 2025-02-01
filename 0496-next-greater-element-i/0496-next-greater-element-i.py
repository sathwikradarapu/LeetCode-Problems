class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        dici={}
        res=[]
        for i in nums2:
            while stack and stack[-1]<i:
                j=stack.pop()
                dici[j]=i
            stack.append(i)
        for i in stack:
            dici[i]=-1
        for i in nums1:
            res.append(dici[i])
        return res