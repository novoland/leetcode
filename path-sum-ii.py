class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    def pathSum(self, root, sum):
        self.result = []
        if not root:
            return self.result
        self.result = []
        self.path = []
        self.function(root,sum)
        return self.result

    def function(self,node,num):
        if not node.left and not node.right:
            if node.val == num:
                self.path.append(node.val)
                self.result.append(self.path[:])
                self.path.pop()
        else:
            self.path.append(node.val)
            if node.left:
                self.function(node.left,num - node.val)
            if node.right:
                self.function(node.right,num - node.val)   
            self.path.pop()