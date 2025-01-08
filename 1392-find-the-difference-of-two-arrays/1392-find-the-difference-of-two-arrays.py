class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        n1=[]
        for i in nums1:
            if i not in n1 and i not in nums2:
                n1.append(i)
        n2=[]
        for i in nums2:
            if i not in n2 and i not in nums1:
                n2.append(i)
        return [n1,n2]