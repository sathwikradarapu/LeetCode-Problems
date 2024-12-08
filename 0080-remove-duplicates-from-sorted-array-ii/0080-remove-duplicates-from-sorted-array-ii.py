class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=1
        j=1
        n=len(nums)
        count=0
        while i<n:
            if nums[i]==nums[i-1]:
                count+=1
            else:
                count=0
            if count<=1:
                nums[j]=nums[i]
                j+=1
            i+=1
        return j
