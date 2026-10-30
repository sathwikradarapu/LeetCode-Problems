class Solution:
    def search(self, nums: list[int], target: int) -> int:
        length=len(nums)
        for index in range(length):
            if nums[index]==target:
                return index
        return -1