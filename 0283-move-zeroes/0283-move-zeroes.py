class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        for i in nums:
            if i==0:
                b=i
                nums.remove(i)
                nums.append(b)
                
