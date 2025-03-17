class ReverseList:
    def iteration(self, head):
        prev = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev

    def recursion(self, head):
        if not head or not head.next:
            return head
        p = self.recursion(head.next)
        head.next.next = head
        head.next = None
        return p
