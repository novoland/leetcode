# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
    	if not l1 and not l2:
    		return
    	elif not l1:
    		return l2
    	elif not l2:
    		return l1
    	else:
    		node1 = l1
    		node2 = l2
    		head = None
    		if node1.val <= node2.val:
    			head = node1
    			node1 = node1.next
    		else:
    			head = node2
    			node2 = node2.next
    		node = head
    		while node1 or node2:
    			if not node1:
    				node.next = node2
    				break;
    			elif not node2:
    				node.next = node1
    				break;
    			if node1.val <=node2.val:
    				node.next = node1
    				node1 = node1.next
    			else:
    				node.next = node2
    				node2 = node2.next
    			node = node.next
    		return head
   	
        