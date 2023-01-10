# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        right = left = head
        count= 0
        while right.next:
            if right.next.next is None:
                return left.next
            right = right.next.next
            left = left.next
        
        return left