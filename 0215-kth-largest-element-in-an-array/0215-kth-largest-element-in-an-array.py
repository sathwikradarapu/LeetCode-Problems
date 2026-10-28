class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        #bruteforce
        nums=sorted(nums,reverse=True)
        return nums[k-1]