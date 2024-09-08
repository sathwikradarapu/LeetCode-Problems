class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        ans=False
        myset=set()
        for i in nums:
            if i in myset:
                ans=True
                break
            else:
                myset.add(i)
        return ans