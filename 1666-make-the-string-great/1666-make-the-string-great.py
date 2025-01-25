class Solution:
    def makeGood(self, s: str) -> str:
        res=[]
        for i in s:
            if len(res)==0:
                res.append(i)
            else:
                a=res[-1]
                b=i
                if (a.islower() and b.isupper()) or (a.isupper() and b.islower()):
                    a=a.lower()
                    b=b.lower()
                    if a==b:
                        res.pop()
                    else:
                        res.append(i)
                else:
                    res.append(i)
        return "".join(res)