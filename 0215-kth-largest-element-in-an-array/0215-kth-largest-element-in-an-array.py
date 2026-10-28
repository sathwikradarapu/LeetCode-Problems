class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        '''#bruteforce
        nums=sorted(nums,reverse=True)
        return nums[k-1]'''

        #optimal
        import heapq
        heap=[]
        for num in nums:
            heapq.heappush(heap,num)
            if len(heap)>k:
                heapq.heappop(heap)
        return heap[0]