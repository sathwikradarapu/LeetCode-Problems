# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length=0
        cur=head
        while cur:
            length+=1
            cur=cur.next
        length=length//2
        cur=head
        count=0
        while cur:
            if count==length:
                return cur
            count+=1
            cur=cur.next