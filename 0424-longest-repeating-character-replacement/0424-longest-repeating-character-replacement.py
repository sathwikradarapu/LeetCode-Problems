class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        n=len(s)
        freq=defaultdict(int)
        ans=float("-inf")
        max_freq=float("-inf")
        for r in range(n):
            freq[s[r]]+=1
            max_freq=max(max_freq,freq[s[r]])
            while (r-l+1)-max_freq>k:
                freq[s[l]]-=1
                l+=1
            ans=max(ans,r-l+1)
        return ans