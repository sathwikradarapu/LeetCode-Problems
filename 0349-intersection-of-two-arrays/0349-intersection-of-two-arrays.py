class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1=set(nums1)
        nums2=set(nums2)
        nums3=set()
        for i in nums1:
            if i in nums2:
                nums3.add(i)
        for i in nums2:
            if i in nums1:
                nums3.add(i)
        nums3=list(nums3)
        return nums3