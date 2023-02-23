# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head
        result = temp_odd = odd = ListNode()
        temp_even = even = ListNode()
        count = 0
        while head:
            if count % 2 == 1:
                even.next = head
                even = even.next
            else:
                odd.next = head
                odd = odd.next
            count += 1
            head = head.next
        even.next = None
        odd.next = temp_even.next
        return result.next
        