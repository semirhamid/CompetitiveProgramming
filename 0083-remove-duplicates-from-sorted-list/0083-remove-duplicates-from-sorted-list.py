# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = nex = head
        
        if head==None : 
            return None
        if head.next is None:
            return head
        while head.next is not None:
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next
                
        return nex