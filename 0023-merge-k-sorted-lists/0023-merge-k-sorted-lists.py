class Solution:
    def mergeKLists(self, lists) :
        if not lists or  len(lists) == 0:
            return None

        while len(lists)>1:
            merged_hold = []
            for i in range(0,len(lists),2):
                L1 = lists[i]
                L2 = lists[i + 1] if (i +1) < len(lists) else None
                merged_hold.append(self.merged_sort(L1, L2))
            lists = merged_hold
        return lists[0]

    def merged_sort(self, LL1 , LL2):
        pointer = ListNode()
        dummy = pointer
        while LL1 and LL2:
            if LL1.val < LL2.val:
                dummy.next = LL1
                LL1 = LL1.next
            else:
                dummy.next = LL2
                LL2 = LL2.next
            dummy = dummy.next

        if LL1:
            dummy.next = LL1
        if LL2:
            dummy.next = LL2
        return pointer.next