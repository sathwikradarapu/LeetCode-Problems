class Solution:
    def myAtoi(self, s: str) -> int:
        num='0123456789'
        sign='-+'
        res=""
        for x in s:
            if x==' ' and len(res)==0:
                continue
            elif (x in sign) and len(res)==0:
                res+=x
            elif (x in num) and x!=0:
                res+=x
            elif (x in num) and x==0 and (res in sign):
                continue
            elif (x in num) and x==0:
                res+=x
            else:
                break
        if res=='' or res in sign:
            return 0
        else:
            if int(res)<-(2**31):
                return -(2**31)
            elif int(res)>(2**31-1):
                return (2**31-1)
            else:
                return int(res)