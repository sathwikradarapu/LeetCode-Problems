class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums=sorted(nums)
        set_nums=set()
        ans=[]
        for i in nums:
            if i not in set_nums:
                set_nums.add(i)
            else:
                ans.append(i)
        return ans