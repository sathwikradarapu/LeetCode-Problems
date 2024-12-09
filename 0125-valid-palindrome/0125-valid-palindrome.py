import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        res=""
        for i in s:
            if i.isalpha():
                if i.isupper():
                    res+=i.lower()
                else:
                    res+=i
            if i.isdigit():
                res+=i
        
        return res==res[::-1]