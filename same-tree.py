# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        elif not p and q:
            return False
        elif p and not q:
            return False
        elif p.val != q.val:
            return False
        else:
            l = self.isSameTree(p.left,q.left)
            r = self.isSameTree(p.right,q.right)
            return l and r