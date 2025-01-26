class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for i in range(k):
            a=max(gifts)
            b=gifts.index(a)
            a=int(sqrt(a))
            gifts[b]=a
        return sum(gifts)