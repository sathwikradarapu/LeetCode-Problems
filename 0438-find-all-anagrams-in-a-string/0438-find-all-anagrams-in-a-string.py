class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        l=0
        temp1=""
        temp2=""
        p=sorted(p)
        ans=[]
        for r in range(len(s)):
            temp1+=s[r]
            if r-l==len(p):
                temp1=temp1[1:]
                l+=1
            if r-l+1==len(p):
                temp2=temp1
                temp2=sorted(temp2)
                if p==temp2:
                    ans.append(l)
        return ans
