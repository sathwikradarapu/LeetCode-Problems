class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hash_map={}
        for i in nums:
            if i in hash_map:
                hash_map[i]+=1
            else:
                hash_map[i]=1
        ans=0
        for i in hash_map.values():
            temp=(i*(i-1))//2
            ans+=temp
        return ans