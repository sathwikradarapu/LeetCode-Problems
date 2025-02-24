# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        first=1
        last=n
        while first<=last:
            middle=(first+last)//2
            if isBadVersion(middle):
                last=middle-1
            else:
                first=middle+1
        return first