class Solution:
    def search(self, nums: list[int], target: int) -> int:
        '''#bruteforce
        length=len(nums)
        for index in range(length):
            if nums[index]==target:
                return index
        return -1'''

        # optimal
        length = len(nums)

        if length == 0:
            return -1

        left = 0
        right = length - 1

        # Step 1: Find pivot
        while left < right:
            middle = (left + right) // 2

            if nums[middle] > nums[right]:
                left = middle + 1
            else:
                right = middle

        pivot = left

        # Step 2: Decide search range
        left = 0
        right = length - 1

        if target >= nums[pivot] and target <= nums[right]:
            left = pivot
        else:
            right = pivot - 1

        # Step 3: Binary search
        while left <= right:
            middle = (left + right) // 2

            if target > nums[middle]:
                left = middle + 1

            elif target == nums[middle]:
                return middle

            else:
                right = middle - 1

        return -1