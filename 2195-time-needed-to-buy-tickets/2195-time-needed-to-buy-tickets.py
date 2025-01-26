from collections import deque

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        tickets=deque(tickets)
        time=0
        while True:
            time+=1
            tickets[0]-=1
            if k==0 and tickets[0]==0:
                break
            if tickets[0]==0:
                tickets.popleft()
            else:
                tickets.append(tickets.popleft())
            if k>0:
                k=k-1
            else:
                k=len(tickets)-1
        return time