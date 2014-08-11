# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        tmp = []
        nodePre = head
        node = head
        if not head:
        	return head
        elif not head.next:
        	return head
        else:
        	node = head.next  
        	tmp.append(head.val)    
        
        while node:
        	if node.val in tmp:
        		nodePre.next = node.next
        		node = node.next
        	else:
        		tmp.append(node.val)
        		nodePre = node
        		node = node.next	
        return head
