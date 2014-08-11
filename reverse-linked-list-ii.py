class Solution:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):
        if not head:
            return
        if m == n:
            return head
        node = head
        for x in xrange(1,m-1,1):
            node = node.next
        t = node.next if m != 1 else node
        ne = node.next if m != 1 else node
        sub = None
        for x in xrange(m,n+1,1):
            cur = ne
            ne = ne.next
            cur.next = sub 
            sub = cur    
        t.next = ne
        if m == 1:
            head = sub
        else:
            node.next = sub
        return head