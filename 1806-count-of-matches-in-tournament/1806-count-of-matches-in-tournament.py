class Solution:
    def numberOfMatches(self, n: int) -> int:
        ans=0
        while n>1:
            if n%2==1:
                matches=(n-1)//2
                teams=n-matches
            else:
                matches=n//2
                teams=n-matches
            ans+=matches
            n=teams
        return ans