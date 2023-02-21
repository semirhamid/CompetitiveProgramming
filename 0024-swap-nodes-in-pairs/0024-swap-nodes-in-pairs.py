# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        right = left = dummy
        while right and right.next and right.next.next:
            first = right.next
            second = first.next
            first.next = second.next
            second.next = first
            right.next = second
            right = right.next.next
        return dummy.next
        