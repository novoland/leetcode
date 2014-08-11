# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        if not l1 and not l2:
            return []
        elif not l1:
            return l2
        elif not l2:
            return l1
        node1 = l1
        node2 = l2
        result = None
        node3 = None
        flag = 0
        while node1 and node2:
            n = node1.val + node2.val + flag
            flag = n / 10
            if result:
                node3.next = ListNode(n%10)
                node3 = node3.next
            else:
                result = ListNode(n%10)
                node3 = result
            node1 = node1.next
            node2 = node2.next
        while node1:
            n = node1.val + flag
            flag = n / 10
            if result:
                node3.next = ListNode(n%10)
                node3 = node3.next
            else:
                result = ListNode(n%10)
                node3 = result
            node1 = node1.next
        while node2:
            n = node2.val + flag
            flag = n / 10
            if result:
                node3.next = ListNode(n%10)
                node3 = node3.next
            else:
                result = ListNode(n%10)
                node3 = result
            node2 = node2.next    
        if flag:
            node3.next = ListNode(flag)  
        return result    