class Solution:
    def isPalindrome(self, s: str) -> bool:
        def innerFunction(l,r,s):
            nonlocal ans
            if l>=r:
                return
            else:
                if not s[l].isalnum():
                    innerFunction(l+1,r,s)
                elif not s[r].isalnum():
                    innerFunction(l,r-1,s)
                else:
                    if s[l].lower()==s[r].lower():
                        innerFunction(l+1,r-1,s)
                    else:
                        ans=False
                        return
        l=0
        r=len(s)-1
        ans=True
        innerFunction(l,r,s)
        return ans