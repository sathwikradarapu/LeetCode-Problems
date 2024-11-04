class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        count=0
        min_ele=min(nums)
        while min_ele<k:
            nums.remove(min_ele)
            count+=1
            min_ele=min(nums)
        return count
        