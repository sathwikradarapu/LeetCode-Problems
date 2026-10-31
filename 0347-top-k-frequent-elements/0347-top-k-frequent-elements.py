class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #optimal
        hash_map={}
        length=len(nums)
        for index in range(length):
            number=nums[index]
            if number not in hash_map:
                hash_map[number]=1
            else:
                hash_map[number]+=1
        sorted_hash_map=dict(sorted(hash_map.items(),reverse=True,key=lambda item:item[1]))
        return(list(sorted_hash_map.keys())[:k])

        
        