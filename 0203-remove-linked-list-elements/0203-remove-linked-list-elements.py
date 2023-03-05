# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        returned = dummy = ListNode()
        dummy.next = head
        
        def removeItem(hd):
            if hd == None or  hd.next == None:
                return
            while hd and hd.next and hd.next.val == val:
                temp = hd.next.next
                hd.next = temp
            removeItem(hd.next)
        removeItem(dummy)
        return returned.next
                
                
            