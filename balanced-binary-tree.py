# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        if not root:
            return True
        self.isBalanced = True
        self.deal(root)
        return self.isBalanced

    def deal(self,root):
        if not self.isBalanced:
            return 0 
        if not root:
            return 0
        left = self.deal(root.left)
        right = self.deal(root.right)
        heigth = max(left,right)+1
        if abs(left-right)>1:
            self.isBalanced = False
        return heigth

                