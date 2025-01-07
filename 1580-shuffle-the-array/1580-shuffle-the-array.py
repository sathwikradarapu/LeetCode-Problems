class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        l1=[]
        j=n
        for i in range(n):
            l1.extend([nums[i],nums[j]])
            j+=1
        return l1