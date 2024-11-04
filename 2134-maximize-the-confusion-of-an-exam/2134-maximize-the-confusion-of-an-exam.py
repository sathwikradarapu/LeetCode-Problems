class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        n=len(answerKey)
        ct=0
        cf=0
        l=0
        ans=float("-inf")
        for r in range(n):
            if answerKey[r]=='T':
                ct+=1
            else:
                cf+=1
            while(min(ct,cf)>k):
                if answerKey[l]=='T':
                    ct-=1
                else:
                    cf-=1
                l+=1
            ans=max(ans,r-l+1)
        return ans