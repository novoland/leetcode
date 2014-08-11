# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
    	if not head:
    		return
    	cur = head
    	while cur:
    		node = RandomListNode(cur.label)
    		node.next = cur.next
    		cur.next = node
    		cur = node.next
    	cur = head
    	while cur:
    		if cur.random:
    			cur.next.random = cur.random.next
    		cur = cur.next.next
    	newhead = head.next
    	cur = head.next.next
    	slow = head
    	fast = newhead
    	while cur:
    		slow.next = cur
    		fast.next = cur.next
    		cur = cur.next.next
    		slow = slow.next
    		fast = fast.next
        slow.next = None
    	return newhead
        