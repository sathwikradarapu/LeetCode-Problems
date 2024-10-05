class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums=sorted(nums)
        test_case=len(nums)//2
        return nums[test_case]
                
