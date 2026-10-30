class Solution:
    def search(self, nums: list[int], target: int) -> int:
        '''#bruteforce
        length=len(nums)
        for index in range(length):
            if nums[index]==target:
                return index
        return -1'''

        #mini_element = min(nums)
        #mini_element_index = nums.index(mini_element)

        left=0
        right=len(nums)-1
        while left<right:
            middle=(left+right)//2
            if nums[middle]>nums[right]:
                left=middle+1
            else:
                right=middle
        mini_element_index=left

        if target >= nums[mini_element_index] and target <= nums[-1]:
            left = mini_element_index
            right = len(nums) - 1
        else:
            left = 0
            right = mini_element_index - 1

        while left <= right:
            middle = (left + right) // 2

            if nums[middle] == target:
                return middle

            elif target > nums[middle]:
                left = middle + 1

            else:
                right = middle - 1

        return -1