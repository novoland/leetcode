# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param preorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return
        if len(preorder) == 1 and len(inorder) == 1 and preorder[0] == inorder[0]:
            return TreeNode(preorder[0])
        value = preorder[0]
        node = TreeNode(value)
        index = 0
        for x in xrange(0,len(inorder),1):
            if inorder[x] == value:
                index = x
                break
        node.left = self.buildTree(preorder[1:index+1],inorder[:index])
        node.right = self.buildTree(preorder[index+1:],inorder[index+1:])
        return node
        