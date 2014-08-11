class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def sortList(self, head):
        if not head or not head.next:
            return head
        slow,fast=head,head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        head1 = head
        head2 = slow.next
        slow.next = None
        a = self.sortList(head1)
        b = self.sortList(head2)
        return  self.merge(a,b)

    def merge(self,head1,head2):
        if not head1:
            return head2
        if not head2:
            return head1
        head= ListNode(0)
        cur,cur1,cur2=head,head1,head2
        while cur1 and cur2 :
            if cur1.val <= cur2.val:
                cur.next = cur1
                cur = cur.next
                cur1 = cur1.next
            elif cur1.val > cur2.val:
                cur.next = cur2
                cur = cur.next
                cur2 = cur2.next
        if cur1:
            cur.next = cur1
        if cur2:
            cur.next = cur2          
        return head.next