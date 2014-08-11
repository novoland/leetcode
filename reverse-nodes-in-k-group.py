class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverseKGroup(self, head, k):
        if not head:
            return head
        cur,start = head,head
        newhead,node=None,head
        while cur:
            flag = False
            for x in xrange(1,k):
                if cur.next:
                    cur = cur.next
                else:
                    flag = True
            if cur:
                t=cur.next
                cur.next = None
                cur = t
            if not newhead:
                newhead = self.reverseList(start) if not flag else start
                start = cur
            else:
                node.next = self.reverseList(start) if not flag else start
                node = start
                start = cur
        return newhead


    def reverseList(self,head):
        if not head:
            return
        cur = head
        newhead = None
        while cur:
            newhead,newhead.next,cur = cur,newhead,cur.next
        return newhead