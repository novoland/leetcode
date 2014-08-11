class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        if not head or not head.next or self.check(head):
            return head
        
        cur = head.next
        head.next = None
        while cur:
            node = cur
            cur = cur.next
            node.next = None
            point = head
            pre = None
            while point:
                if point.val > node.val:
                    break
                else:
                    pre = point
                    point = point.next
            if pre:
                pre.next = node                
            else:
                head = node
            node.next = point                
        return head

    def check(self,head):
        node = head
        while node.next:
            if node.next.val < node.val:
                return False
            node = node.next
        return True