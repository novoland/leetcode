# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrderBottom(self, root):
        if not root:
            return []
        result = []
        stack = [[],[]]
        cur,pre=0,1
        stack[cur] = [root]
        while True:
            cur,pre = pre,cur
            if not stack[pre]:
                break
            path = []
            for x in stack[pre]:
                path.append(x.val)
            result.append(path)
            stack[cur]=[]
            stack[pre].reverse()
            while stack[pre]:
                node = stack[pre].pop()
                if node.left:
                    stack[cur].append(node.left)
                if node.right:
                    stack[cur].append(node.right)  
        result.reverse()
        return result                   

        