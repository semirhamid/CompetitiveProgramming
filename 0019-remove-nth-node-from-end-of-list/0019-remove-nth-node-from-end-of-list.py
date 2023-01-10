# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head, n):
        first_pointer = second_pointer = head
        for _ in range(n):
            first_pointer = first_pointer.next
        if not first_pointer:
            return head.next
        while first_pointer.next:
            first_pointer = first_pointer.next
            second_pointer = second_pointer.next
        second_pointer.next = second_pointer.next.next
        return head