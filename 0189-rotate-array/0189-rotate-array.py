class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l1=nums
        for i in range(k):
            a=l1.pop()
            l1.insert(0,a)
        nums[:]=l1