class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        if not root:
            return
        self.f(root)

    def f(self,root):
        if not root.left and not root.right:
            return root
        elif not root.left and root.right:
            return self.f(root.right)
        elif root.left and not root.right:
            t = self.f(root.left)
            root.right = root.left
            root.left = None
            return t
        else:
            t = self.f(root.left)
            n = self.f(root.right)
            t.right = root.right
            root.right = root.left            
            root.left = None
            return n