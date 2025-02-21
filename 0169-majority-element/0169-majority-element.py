class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dici={}
        for i in nums:
            if i in dici:
                dici[i]+=1
            else:
                dici[i]=1
        ans=max(list(dici.values()))
        for num,freq in dici.items():
            if freq==ans:
                return num