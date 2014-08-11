# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        if not root:
            return []
        stack = [[root,False]]
        path = []
        while stack:
            cur = stack.pop()
            node = cur[0]
            visited = cur[1]
            if visited:
                path.append(node.val)
            else:
                if node.right:
                    stack.append([node.right,False])
                stack.append([node,True])
                if node.left:
                    stack.append([node.left,False])
        return path 
        