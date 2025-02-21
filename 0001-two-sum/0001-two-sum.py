class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map={}
        n=len(nums)
        for i in range(n):
            a=nums[i]
            s=target-a
            if s in hash_map:
                return [hash_map[s],i]
            else:
                hash_map[a]=i