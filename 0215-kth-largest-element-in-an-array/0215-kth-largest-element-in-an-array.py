class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        nums=sorted(nums,reverse=True)
        return nums[k-1]