# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr=[]
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
        return True