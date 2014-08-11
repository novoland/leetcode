class Solution:
    # @param root, a tree node
    # @return an integer
    def maxPathSum(self, root):
        if not root:
            return 0
        t = self.deal(root)
        return t[0]
    
    def deal(self,root):
        if not root:
            return [-100000,-100000]
        if not root.left and not root.right:
            return [root.val,root.val]
        left = self.deal(root.left)
        right = self.deal(root.right)
        # print left
        # print right
        maxb = max(left[1]+root.val,right[1]+root.val,root.val)
        maxa = max(left[0],right[0],maxb,left[1],right[1],left[1]+root.val+right[1])
        # print [maxa,maxb]
        return [maxa,maxb]