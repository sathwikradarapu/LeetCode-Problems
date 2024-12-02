from typing import List

class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        i, j = 0, 0
        dist = 0
        n, m = len(nums1), len(nums2)
        
        while i < n and j < m:
            if nums1[i] <= nums2[j]:
                dist = max(dist, j - i)
                j += 1  # Move j forward to try for a larger distance
            else:
                i += 1  # Move i forward to satisfy nums1[i] <= nums2[j]
        
        return dist
