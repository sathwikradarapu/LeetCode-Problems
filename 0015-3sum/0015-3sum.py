class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        length=len(nums)
        answer=[]
        for left in range(length-2):
            if left>0 and nums[left]==nums[left-1]:
                continue
            middle=left+1
            right=length-1
            while middle<right:
                total=nums[left]+nums[middle]+nums[right]
                if total==0:
                    answer.append([nums[left],nums[middle],nums[right]])
                    while middle<right and nums[middle]==nums[middle+1]:
                        middle+=1
                    while middle<right and nums[right]==nums[right-1]:
                        right-=1
                    middle+=1
                    right-=1
                elif total>0:
                    right-=1
                else:
                    middle+=1
        return answer