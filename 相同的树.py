class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def fun(p,q):
            if p==None or q==None:  #两者有一个为None 说明到叶子节点了
                if p==None and q==None:  #都为空,返回真
                    return True
                else:   #否则为假
                    return False
            if p.val!=q.val: #如果不是叶子节点,节点的值不一样就返回假
                return False
            #值一样,咱们就继续往下看
            return fun(p.left,q.left) and fun(p.right,q.right)
        return fun(p,q)