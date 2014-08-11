# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        if not root:
            return False
        if not root.left and not root.right:
            if sum == root.val:
                return True
            else:
                return False
        a = b = False
        if root.left:
            a = self.hasPathSum(root.left,sum-root.val)
        if  root.right:
            b = self.hasPathSum(root.right,sum-root.val)
        return a or b
            