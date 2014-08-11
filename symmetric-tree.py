# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric2(self, a, b):
        if not a and not b:
            return True
        elif a and b:
            if a.val == b.val:
                return self.isSymmetric2(a.left,b.right) and self.isSymmetric2(a.right,b.left)
            else:
                return False     
        else:
            return False    
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        if not root:
            return True
        if not root.left and not root.right:
            return True
        elif root.left and root.right:
            return self.isSymmetric2(root.left, root.right)
        else:
            return False