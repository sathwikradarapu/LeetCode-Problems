class Solution:
    def isPalindrome(self, s: str) -> bool:
        def palindrome(s, l, r):
            nonlocal ans
            
            if l >= r:
                return
            else:
                if not s[l].isalnum():
                    palindrome(s, l + 1, r)
                elif not s[r].isalnum():
                    palindrome(s, l, r - 1)
                else:
                    if s[l].lower() == s[r].lower():
                        palindrome(s, l + 1, r - 1)
                    else:
                        ans = False
                        return
        l = 0
        r = len(s) - 1
        ans = True
        palindrome(s, l, r)
        return ans
