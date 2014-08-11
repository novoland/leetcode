class Solution:
    # @param root, a tree node
    # @return a tree node
    def recoverTree(self, root):
        if not root:
            return
        cur = root
        pre = None
        data = []
        while cur:
            if cur.left:
                tmp = cur.left
                while tmp.right and tmp.right != cur:
                    tmp = tmp.right
                if tmp.right:   
                    if pre and pre.val > cur.val:
                        data.append([pre,cur])
                    pre = cur
                    tmp.right = None
                    cur = cur.right
                else:
                    tmp.right = cur
                    cur = cur.left
            else:
                if pre and pre.val > cur.val:
                    data.append([pre,cur])
                pre = cur 
                cur = cur.right
        if len(data) == 1:
            data[0][0].val,data[0][1].val=data[0][1].val,data[0][0].val
        else:
            data[0][0].val,data[1][1].val=data[1][1].val,data[0][0].val
        return root