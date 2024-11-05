class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hash_map={}
        ans=[]
        for i in nums:
            if i in hash_map:
                hash_map[i]+=1
            else:
                hash_map[i]=1
        for i in hash_map:
            if hash_map[i]>len(nums)/3:
                ans.append(i)
        return ans