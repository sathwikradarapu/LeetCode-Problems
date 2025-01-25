# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        # Collect all values from the linked list
        while head:
            arr.append(head.val)
            head = head.next
        
        # Sort the values
        arr.sort()
        
        # Create a new sorted linked list
        dummy = ListNode()  # Dummy node to simplify construction
        temp = dummy
        for val in arr:
            temp.next = ListNode(val)  # Create a new node for each value
            temp = temp.next  # Move to the next node
        
        return dummy.next  # Return the head of the sorted linked list
