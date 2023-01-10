# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less_than = less_point = ListNode()
        greater_than = great_point = ListNode()
        while head:
            if head.val < x:
                less_than.next = ListNode(head.val)
                less_than = less_than.next
            else:
                greater_than.next = ListNode(head.val)
                greater_than = greater_than.next
            head = head.next
        less_than.next = great_point.next
        return less_point.next
                