class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        '''#bruteforce
        nums=sorted(nums,reverse=True)
        return nums[k-1]'''

        #optimal
        import heapq
        heap=[]
        for number in nums:
            heapq.heappush(heap,number)
            length=len(heap)
            if length>k:
                heapq.heappop(heap)
        return heap[0]