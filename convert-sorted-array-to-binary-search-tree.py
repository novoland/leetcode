# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param num, a list of integers
    # @return a tree node
    def sortedArrayToBST(self, num):
        if not num:
            return
        mid = len(num)/2
        node = TreeNode(num[mid])
        node.left = self.sortedArrayToBST(num[:mid])
        node.right = self.sortedArrayToBST(num[mid+1:])
        return node