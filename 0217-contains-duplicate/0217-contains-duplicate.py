class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_set=set()
        for number in nums:
            if number not in hash_set:
                hash_set.add(number)
            else:
                return True
        return False