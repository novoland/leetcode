# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        if not root:
            return []
        stack = [[root,False]]
        top = 0
        path = []
        while stack:
            cur = stack[top]            
            node = cur[0]
            visited = cur[1]
            if visited:
                path.append(node.val)
                stack.pop()
                top -= 1
            else:                
                if node.right:
                    stack.append([node.right,False])
                    top += 1      
                if node.left:
                    stack.append([node.left,False])
                    top += 1  
                cur[1] = True   
        return path 
        