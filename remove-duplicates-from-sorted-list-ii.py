class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if not head or not head.next:
            return head
        pre = None
        cur = head
        ne = head.next
        flag = False
        while ne:
            if ne.val == cur.val:
                flag = True
                ne = ne.next
                if not ne:
                    if pre:
                        pre.next = ne
                    else:
                        head = ne
            else:
                if flag:
                    if pre:
                        pre.next = ne
                    else:
                        head = ne
                    flag = False
                else:
                    pre = cur
                cur = ne
                ne = ne.next
        return head