class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        hash_set=set()
        for i in nums:
            if i!=0 and i not in hash_set:
                hash_set.add(i)
        return len(hash_set)

        