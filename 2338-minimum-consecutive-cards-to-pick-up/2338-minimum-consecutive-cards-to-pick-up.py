class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        n=len(cards)
        hash_map={}
        ans=float('inf')
        for i in range(n):
            num=cards[i]
            if num not in hash_map:
                hash_map[num]=i
            else:
                index=hash_map[num]
                ans=min(ans,i-index+1)
                hash_map[num]=i
        if ans==float('inf'):
            return -1
        else:
            return ans