# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        l = r = None
        if root.left:
            l = self.minDepth(root.left)
        if root.right:
            r = self.minDepth(root.right)
        if l and r:
            return 1+l if l < r else r+1
        elif l:
            return 1+l
        else:
            return 1+r