# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if not root:
            return
        stack = [[],[]]
        cur,pre=0,1
        stack[cur]=[root]
        while True:
            cur,pre=pre,cur
            stack[cur]=[]
            length = len(stack[pre])
            for x in xrange(length):
                if stack[pre][x].left:
                    stack[cur].append(stack[pre][x].left)
                if stack[pre][x].right:
                    stack[cur].append(stack[pre][x].right)
                stack[pre][x].next=stack[pre][x+1] if x < length-1  else None
            if not stack[cur]:
                break
