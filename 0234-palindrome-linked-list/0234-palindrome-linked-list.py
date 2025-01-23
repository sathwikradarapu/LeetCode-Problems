# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow=head
        fast=head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        
        prev=None
        curr=slow
        while slow:
            nxt=slow.next
            slow.next=prev
            prev=slow
            slow=nxt
        
        left,right=head,prev
        while right:
            if left.val!=right.val:
                return False
            left=left.next
            right=right.next
        return True

        ''' arr=[]
        temp=head
        while temp:
            arr.append(temp.val)
            temp=temp.next
        i=0
        j=len(arr)-1
        while i<=j:
            if arr[i]!=arr[j]:
                return False
            i+=1
            j-=1
        return True '''