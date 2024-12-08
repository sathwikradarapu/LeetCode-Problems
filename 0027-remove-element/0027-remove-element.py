class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i=0
        j=0
        n=len(nums)
        while i<n:
            if nums[i]!=val:
                nums[j]=nums[i]
                i+=1
                j+=1
            else:
                i+=1
        return j