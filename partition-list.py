# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
        if not head:
            return
        low,high,cur,lc,hc=None,None,head,None,None
        while cur:
            if cur.val < x:
                if not low:
                    low = cur
                    lc = low
                else:
                    lc.next = cur
                    lc = lc.next
            else:
                if not high:
                    high = cur
                    hc = cur
                else:
                    hc.next=cur
                    hc = hc.next
            cur = cur.next
        if low:
            lc.next = high            
        else:
            low = high
        if hc:
            hc.next = None
        return low