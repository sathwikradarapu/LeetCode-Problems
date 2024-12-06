class Solution:
    def partitionString(self, s: str) -> int:
        partitions = 0
        seen = set()  # To track characters in the current substring
        
        for char in s:
            if char in seen:
                # Start a new substring
                partitions += 1
                seen.clear()
            seen.add(char)
        
        # Count the last substring
        return partitions + 1