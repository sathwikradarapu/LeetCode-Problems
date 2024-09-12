class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map={}
        for i in range(0,len(nums)):
            search=target-nums[i]
            if search in hash_map:
                return [i,hash_map[search]]
            else:
                hash_map[nums[i]]=i