# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        if not head:
            return None  
        node1 = head                    
        node2 = head.next    
        if not node2:
            return node1
        elif node2 and not node2.next:
            head = node2
            node2.next = node1
            node1.next = None
        else:
            head = node2
            tmp = node2.next
            node2.next = node1
            node1.next = self.swapPairs(tmp)
        return head
        