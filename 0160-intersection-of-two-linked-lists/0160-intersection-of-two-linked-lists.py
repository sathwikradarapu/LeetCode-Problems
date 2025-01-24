# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # Use a set to store visited nodes from list A
        visited_nodes = set()
        
        # Traverse list A and store each node in the set
        while headA:
            visited_nodes.add(headA)
            headA = headA.next
        
        # Traverse list B and check if any node is in the set
        while headB:
            if headB in visited_nodes:
                return headB  # Return the intersecting node
            headB = headB.next
        
        # If no intersection is found
        return None
