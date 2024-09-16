class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set=set(nums)
        max_len=0
        for i in nums_set:
            if i-1 in nums_set:
                continue
            else:
                current_num=i
                current_streak=1
                while current_num+1 in nums_set:
                    current_num+=1
                    current_streak+=1
                max_len=max(max_len,current_streak)
        return max_len