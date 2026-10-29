class Solution(object):
    def twoSum(self, nums, target):
        #bruteforce
        length=len(nums)
        for index1 in range(length-1):
            for index2 in range(index1+1,length):
                number1=nums[index1]
                number2=nums[index2]
                if number1+number2==target:
                    return [index1,index2]
        return -1
        