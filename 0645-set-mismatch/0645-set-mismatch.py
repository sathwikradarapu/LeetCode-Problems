class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        s=set()
        dup=-1
        mis=-1
        for i in nums:
            if i not in s:
                s.add(i)
            else:
                dup=i
                
        for i in range(1,len(nums)+1):
            if i not in s:
                mis=i
               
        return [dup,mis]