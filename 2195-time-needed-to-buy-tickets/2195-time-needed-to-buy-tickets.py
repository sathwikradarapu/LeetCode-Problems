from collections import deque

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        tickets = deque(tickets)  # Convert the list to a deque
        time = 0
        
        while True:
            # Process the person at the front of the queue
            time += 1  # 1 second passes as the person buys a ticket
            tickets[0] -= 1  # Reduce the number of tickets they need
            
            # Check if the person at position `k` has finished
            if tickets[0] == 0 and k == 0:
                break
            
            # Move the person to the back of the queue or remove them if they’re done
            if tickets[0] == 0:
                tickets.popleft()  # Remove the person if they’ve bought all tickets
            else:
                tickets.append(tickets.popleft())  # Move the person to the back of the line
            
            # Update `k` to track the person's new position
            k = k - 1 if k > 0 else len(tickets) - 1
        
        return time
