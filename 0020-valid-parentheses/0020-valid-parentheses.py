class Solution:
    def isValid(self, s: str) -> bool:
        a=['(','[','{']
        b=[')',']','}']
        c=[]
        for i in s:
            if i in a:
                c.append(i)
            else:
                if len(c)!=0:
                    if (i==b[0] and c[-1]==a[0]) or (i==b[1] and c[-1]==a[1]) or (i==b[2] and c[-1]==a[2]):
                        c.pop()
                    else:
                        return False
                else:
                    return False
        if len(c)==0:
            return True
        else:
            return False