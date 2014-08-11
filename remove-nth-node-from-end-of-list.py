class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        if not head:
            return
        if not n:
            return head
        fast = head
        slow = head
        cur = head
        for x in xrange(0,n,1):
            if not fast:
                return head            
            fast = fast.next

        while fast:
            fast = fast.next
            cur = slow
            slow = slow.next
        if slow == cur:
            head = cur.next
        else:
            cur.next = slow.next
        return head