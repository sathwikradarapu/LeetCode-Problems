class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        cond=(n//2)
        dici={}
        for i in nums:
            if i in dici:
                dici[i]+=1
            else:
                dici[i]=1
        for num,freq in dici.items():
            if freq>cond:
                return num