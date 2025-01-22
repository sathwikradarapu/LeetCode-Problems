class Solution:
    def hammingWeight(self, n: int) -> int:
        res=""
        while n:
            res+=str(n%2)
            n=n>>1
        return res[::-1].count('1')