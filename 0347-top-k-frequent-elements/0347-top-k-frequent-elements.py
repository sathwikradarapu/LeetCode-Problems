class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        for i in range(len(nums)):
            if nums[i] in hash_map:
                hash_map[nums[i]] += 1
            else:
                hash_map[nums[i]] = 1
        sorted_hash_map=dict(sorted(hash_map.items(),key=lambda item:item[1],reverse=True ))
        ans=list(sorted_hash_map.keys())[:k]
        return ans

        
        