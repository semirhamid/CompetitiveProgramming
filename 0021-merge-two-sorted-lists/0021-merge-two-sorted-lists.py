# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur = helper = ListNode()
        while list1 and list2:               
            if list1.val < list2.val:
                cur.next = list1
                list1, cur = list1.next, list1
            else:
                cur.next = list2
                list2, cur = list2.next, list2
                
        if list1 or list2:
            cur.next = list1 if list1 else list2
            
        return helper.next
 # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = dummy = ListNode()
        def merge(l1, l2, result):
            if l1 == None:
                result.next = l2
                return result
            if l2 == None:
                result.next = l1
                return result
            if l1.val < l2.val:
                result.next = l1
                result = result.next
                l1 = l1.next
                return merge(l1, l2, result)
            else:
                result.next = l2
                result = result.next
                l2 = l2.next
                return merge(l1, l2, result)
        merge(list1, list2, result)
        return dummy.next
