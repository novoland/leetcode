class Solution:
    # @param head, a list node
    # @return a tree node
    def sortedListToBST(self, head):
        if not head:
            return
        node = head
        n = 0
        while node:
            n += 1
            node = node.next
        self.list = head
        return self.sort(head,0,n-1)
        
    def sort(self,head,start,end):
        # print '----'
        # print start
        # print end        
        if start > end:
            return
        mid = (start+end)/2


        # left = self.sort(head,start,mid-1)
        # node = TreeNode(head.val)
        # print head.val
        # node.left = left
        # head = head.next
        # # print head.val
        # node.right = self.sort(head,mid+1,end)

        left = self.sort(self.list,start,mid-1)
        node = TreeNode(self.list.val)
        node.left = left
        self.list = self.list.next
        # print head.val
        node.right = self.sort(self.list,mid+1,end)
        return node