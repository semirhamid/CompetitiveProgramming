# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        cur, nxt, pre = dummy, dummy, dummy
        cnt = 0
        while cur.next:
            cnt += 1
            cur = cur.next
            
        while cnt >= k:
            cur = new = pre.next
            nxt = cur.next
            for _ in range(k-1):
                tmp = nxt.next
                nxt.next = cur
                cur = nxt
                nxt = tmp
            
            pre.next = cur
            new.next = nxt
            pre = new
            cnt -= k
            
        return dummy.next
        