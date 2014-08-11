# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
    	if not head or not head.next:
    		return head
    	tmp = []
    	cur = head
    	i,size =1,0
    	while cur:
    		tmp.append(cur)
    		cur = cur.next
    		size += 1
    	cur = head
    	next = head.next
    	while i < size:
    		if i % 2 != 0:
    			cur.next = tmp.pop()
    		else:
    			cur.next = next	
    			next = next.next
    		cur = cur.next
    		i += 1
    	cur.next = None
    	return head