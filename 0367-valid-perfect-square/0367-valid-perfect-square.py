class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left=1
        right=num
        while left<=right:
            middle=(left+right)//2
            if middle*middle>num:
                right=middle-1
            elif middle*middle<num:
                left=middle+1
            else:
                return True
        return False