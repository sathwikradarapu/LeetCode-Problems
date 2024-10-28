from typing import List

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        emp=''
        for i in range(len(nums)):
            if nums[i][i]=='0':
                emp+='1'
            else:
                emp+='0'
        return emp