class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        dic={}
        for i in nums:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
            if dic[i]*2>len(nums):
                dom=i
        left=0
        right=dic[dom]
        for i in range(len(nums)):  
            if nums[i]==dom:
                left+=1
                right-=1
            if ((left*2)>(i+1)) and (right*2)>(len(nums)-i-1):
                return i
        return -1
            