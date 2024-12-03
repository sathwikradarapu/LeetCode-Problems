class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums_set=set()
        for i in nums:
            if i not in nums_set:
                nums_set.add(i)
            else:
                return i