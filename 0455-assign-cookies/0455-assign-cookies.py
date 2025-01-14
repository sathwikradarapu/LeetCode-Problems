class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # Sort the greed factors and cookie sizes
        g.sort()
        s.sort()
        
        # Initialize pointers for g and s
        i = 0
        j = 0
        
        # Use the two pointers to find the maximum number of content children
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                # The cookie is big enough to satisfy the child
                i += 1  # Move to the next child
            # Move to the next cookie
            j += 1
        
        # The number of content children is i
        return i