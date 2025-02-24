class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        res=1
        i=1
        while res<=num:
            res=i*i
            if res==num:
                return True
            i+=1
        return False
