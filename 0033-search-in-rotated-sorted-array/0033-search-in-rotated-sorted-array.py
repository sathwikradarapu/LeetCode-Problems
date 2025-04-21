class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        
        length=len(nums)
        left=0
        right=length-1

        #finding smallest value index where rotation is done
        while left<right:
            middle=(left+right)//2
            if nums[middle]>nums[right]:
                left=middle+1
            else:
                right=middle
        small_index=left

        #as rotation is done there will be 2 sorted arrays
        #finding in which sorted array the element should be searched
        left=0
        right=length-1
        if target>=nums[small_index] and target<=nums[right]:
            left=small_index
        else:
            right=small_index-1

        #use tradtional binary search to find element
        while left<=right:
            middle=(left+right)//2
            if nums[middle]==target:
                return middle
            elif nums[middle]>target:
                right=middle-1
            else:
                left=middle+1
        return -1