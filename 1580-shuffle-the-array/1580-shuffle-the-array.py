class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        l1=nums[:n]
        l2=nums[n:]
        l3=[]
        for i in range(n):
            l4=[l1[i],l2[i]]
            l3.extend(l4)
        return l3