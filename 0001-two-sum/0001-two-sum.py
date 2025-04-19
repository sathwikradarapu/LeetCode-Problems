class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map={}
        length=len(nums)
        for index in range(length):
            number=nums[index]
            search=target-number
            if search not in hash_map:
                hash_map[number]=index
            else:
                return [index,hash_map[search]]