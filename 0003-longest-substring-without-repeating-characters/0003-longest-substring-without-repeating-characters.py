class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        n=len(s)
        hashset=set()
        ans=0
        for r in range(n):
            if s[r] not in hashset:
                hashset.add(s[r])
            else:
                while s[r] in hashset:
                    hashset.remove(s[l])
                    l+=1
                hashset.add(s[r])
            ans=max(ans,r-l+1)
        return ans
            