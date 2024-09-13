class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash_map={}
        for i in range(len(nums)):
            if nums[i] in hash_map:
              hash_map[nums[i]].append(i)
            else:
                hash_map[nums[i]]=[i]
        for i in hash_map.values():
            if len(i)>=1:
                for j in range(len(i)-1):
                    if abs(i[j]-i[j+1])<=k:
                        return True
        return False