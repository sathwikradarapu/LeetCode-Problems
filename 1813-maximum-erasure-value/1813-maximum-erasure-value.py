class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        l=0
        n=len(nums)
        hash_set=set()
        ans=float("-inf")
        for r in range(n):
            num=nums[r]
            if num not in hash_set:
                hash_set.add(num)
            else:
                while num in hash_set:
                    hash_set.remove(nums[l])
                    l+=1
                hash_set.add(num)
            ans=max(ans,sum(hash_set))
        return ans