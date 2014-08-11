# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def rotateRight(self, head, k):
        if not head or not k or not head.next:
            return head
        fast = head
        slow = head
        for x in xrange(k):
            if fast.next:
                fast = fast.next
            else:
                fast = head
        if fast == slow:
            return head
        while fast.next:
            fast = fast.next
            slow = slow.next
        newhead = slow.next
        slow.next = None
        fast.next = head
        return newhead


