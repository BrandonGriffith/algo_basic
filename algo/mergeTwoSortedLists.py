from typing import Optional

from tests.test_reverseList import ListNode


class MergeTwoSortedLists:
    def iteration(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        mList = node = ListNode()
        while l1 and l2:
            if l1.val > l2.val:
                node.next = l2
                l2 = l2.next
            else:
                node.next = l1
                l1 = l1.next
            node = node.next
        node.next = l1 or l2
        return mList.next

    def recursion(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 or not l2:
            return l1 or l2
        if l1.val > l2.val:
            l2.next = self.recursion(l1, l2.next)
            return l2
        else:
            l1.next = self.recursion(l1.next, l2)
            return l1
