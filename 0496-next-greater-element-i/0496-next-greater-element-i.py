from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Dictionary to store the next greater element for each number in nums2
        next_greater = {}
        stack = []
        
        # Process nums2 using a monotonic decreasing stack
        for num in nums2:
            while stack and stack[-1] < num:
                smaller = stack.pop()
                next_greater[smaller] = num  # Map the smaller element to its next greater element
            stack.append(num)
        
        # Remaining elements in stack have no greater element
        while stack:
            next_greater[stack.pop()] = -1
        
        # Prepare the result for nums1
        return [next_greater[num] for num in nums1]
