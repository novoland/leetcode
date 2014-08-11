# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        if not head or not head.next:
            return False
    	a = head
    	b = head.next.next
    	while(b):
    		if a.val == b.val:
    			return True
    		a = a.next
    		if not b.next:
    		    return False
    		b = b.next.next
    	return False