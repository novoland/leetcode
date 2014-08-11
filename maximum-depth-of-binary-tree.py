# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return left+1 if left > right else right+1
        