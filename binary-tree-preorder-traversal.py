class Solution:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        if not root:
            return []
        stack = [root]
        top = 0
        path = []
        while stack:
            node = stack.pop() 
            path.append(node.val)
            top -= 1        
                           
            if node.right:
                stack.append(node.right)
                top += 1 
            if node.left:
                stack.append(node.left)
                top += 1                  
 
        return path 