# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param inorder, a list of integers
    # @param postorder, a list of integers
    # @return a tree node
    def buildTree(self, inorder, postorder):
        if not inorder or not postorder:
            return
        if len(inorder) == 1 and len(postorder) == 1 and inorder[0] == postorder[0]:
            return TreeNode(inorder[0])
        value = postorder[len(postorder)-1]
        node = TreeNode(value)
        index = len(inorder) -1 
        for x in xrange(0,len(inorder),1):
            if inorder[x] == value:
                index = x
                break;
        node.left = self.buildTree(inorder[:index],postorder[:index])
        node.right = self.buildTree(inorder[index+1:],postorder[index:len(postorder)-1])
        return node