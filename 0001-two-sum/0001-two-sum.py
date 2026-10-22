class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        #brute-force
        '''length=len(nums)
        for index1 in range(length):
            for index2 in range(index1+1,length):
                number1=nums[index1]
                number2=nums[index2]
                result=number1+number2
                if result==target:
                    return [index1,index2]'''
        
        #optimal
        hash_map={}
        length=len(nums)
        for index in range(length):
            number=nums[index]
            search=target-number
            if search in hash_map:
                return [index,hash_map[search]]
            else:
                hash_map[number]=index