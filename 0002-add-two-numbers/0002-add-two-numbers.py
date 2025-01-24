# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = ""
        n2 = ""
        
        # Extract numbers from l1 and l2
        while l1:
            n1 += str(l1.val)
            l1 = l1.next
        while l2:
            n2 += str(l2.val)
            l2 = l2.next
        
        # Convert strings to integers, add them, and convert back to a string
        n1=n1[::-1]
        n2=n2[::-1]
        n3 = str(int(n1) + int(n2))[::-1]
        
        # Convert the result into a linked list
        dummy = ListNode(0)
        current = dummy
        
        for digit in n3:
            current.next = ListNode(int(digit))
            current = current.next
        
        return dummy.next
