class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        set1=set()
        for i in nums:
            if i not in set1:
                set1.add(i)
            else:
                for j in range(1,i):
                    if j not in nums:
                        return [i,j]
                for j in range(i,max(nums)+2):
                    if j not in nums:
                        return [i,j]
