# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # Calculate the lengths of both linked lists
        lenA, lenB = 0, 0
        tempA, tempB = headA, headB
        
        while tempA:
            lenA += 1
            tempA = tempA.next
        
        while tempB:
            lenB += 1
            tempB = tempB.next
        
        # Reset pointers to the start of each list
        tempA, tempB = headA, headB
        
        # Align the starting points of both lists
        if lenA > lenB:
            diff = lenA - lenB
            for _ in range(diff):
                tempA = tempA.next
        elif lenB > lenA:
            diff = lenB - lenA
            for _ in range(diff):
                tempB = tempB.next
        
        # Traverse both lists and find the intersection
        while tempA and tempB:
            if tempA == tempB:
                return tempA  # Intersection node found
            tempA = tempA.next
            tempB = tempB.next
        
        return None  # No intersection
