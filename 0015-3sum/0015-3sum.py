class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        for left in range(n - 2):
            if left > 0 and nums[left] == nums[left - 1]:
                continue  # skip duplicate 'left' values
            middle, right = left + 1, n - 1
            while middle < right:
                total = nums[left] + nums[middle] + nums[right]
                if total == 0:
                    ans.append([nums[left], nums[middle], nums[right]])
                    middle += 1
                    right -= 1
                    # skip duplicates
                    while middle < right and nums[middle] == nums[middle - 1]:
                        middle += 1
                    while middle < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif total > 0:
                    right -= 1
                else:
                    middle += 1
        return ans