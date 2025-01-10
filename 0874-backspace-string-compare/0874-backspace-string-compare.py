class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        a=""
        b=""
        for i in s:
            if i!='#':
                a+=i
            else:
                a=a[:len(a)-1]
        for i in t:
            if i!='#':
                b+=i
            else:
                b=b[:len(b)-1]
        return a==b