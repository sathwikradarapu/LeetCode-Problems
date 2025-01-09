class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split()
        t=[]
        for i in s:
            j=i[::-1]
            t.append(j)
        return " ".join(t)
