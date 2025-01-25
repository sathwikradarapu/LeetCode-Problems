class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hashset = set()
        while head:
            if head in hashset:  # Check if the node itself is in the set
                return True
            hashset.add(head)  # Add the node to the set
            head = head.next
        return False
