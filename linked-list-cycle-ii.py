# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        if not head or not head.next:
        	return 
        fast = head.next.next
        slow = head.next
        isCycle = False
        while fast:
        	if fast == slow:
        		isCycle = True
        		break
        	if not fast.next:
        		return
        	fast = fast.next.next
        	slow = slow.next
        if isCycle:
        	slow = head
        	while slow != fast:
        		slow = slow.next
        		fast = fast.next
        	return slow
        else:
        	return
