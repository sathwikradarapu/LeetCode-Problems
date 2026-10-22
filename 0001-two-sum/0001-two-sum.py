class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        #brute-force
        length=len(nums)
        for index1 in range(length-1):
            for index2 in range(index1+1,length):
                if nums[index1]+nums[index2]==target:
                    return [index1,index2]
    