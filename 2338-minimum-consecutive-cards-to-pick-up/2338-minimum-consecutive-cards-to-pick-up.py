class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        # Dictionary to store the last seen index of each card value
        last_seen = {}
        # Variable to track the minimum length
        min_length = float('inf')  # Start with a large number
        
        for i, card in enumerate(cards):
            # If the card value has been seen before
            if card in last_seen:
                # Calculate the length of the segment
                segment_length = i - last_seen[card] + 1
                # Update the minimum length
                min_length = min(min_length, segment_length)
            # Update the last seen index of the current card
            last_seen[card] = i
        
        # If min_length is not updated, return -1 (no matching pair found)
        return min_length if min_length != float('inf') else -1