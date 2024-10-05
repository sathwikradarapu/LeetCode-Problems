class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash_map={}
        for i in nums:
            if i in hash_map:
                hash_map[i]+=1
            else:
                hash_map[i]=1
        test_case=len(nums)//2
        for i in hash_map:
            if hash_map[i]>test_case:
                return i
                
