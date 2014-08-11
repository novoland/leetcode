class Solution:
    # @param root, a tree node
    # @return a boolean
    def isValidBST(self, root):
        if not root:
            return True
        self.max = None
        return self.f(root)
        

    def  f(self,root):
        if not root.left and not root.right:
            return self.check(root.val)
        elif root.left and not root.right:
            return self.f(root.left) and self.check(root.val)
        elif not root.left and root.right:            
            return self.check(root.val) and self.f(root.right)   
        else:
            return self.f(root.left) and self.check(root.val) and self.f(root.right) 

    def  check(self,value):
        if self.max == None:
            self.max = value
            return True
        else:
            if value > self.max:
                self.max = value
                return True
            else:
                return False