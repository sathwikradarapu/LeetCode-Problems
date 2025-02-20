class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_map={}
        for i in nums:
            if i not in hash_map:
                hash_map[i]=1
            else:
                return True
        return False