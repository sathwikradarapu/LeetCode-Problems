class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        '''for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]
        return [-1,-1]'''

        hash_map={}
        length=len(nums)
        for index in range(length):
            number=nums[index]
            search=target-number
            if search in hash_map:
                return [index,hash_map[search]]
            else:
                hash_map[number]=index
