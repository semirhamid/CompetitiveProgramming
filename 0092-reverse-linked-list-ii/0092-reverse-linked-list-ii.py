class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        result = temp = dummy
        # Move temp to the node before the left position
        for _ in range(left - 1):
            temp = temp.next
        # Reverse the nodes from left to right
        prev, curr = None, temp.next
        for _ in range(right - left + 1):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        # Connect the reversed sublist to the rest of the list
        temp.next.next = curr
        temp.next = prev
        return result.next
