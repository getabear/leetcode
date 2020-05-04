class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 暴力递归超时
        l=[p.val,q.val]

        def fun(root,l):
            if not l:
                return True
            if not root:
                return False
            if root.val in l:
                l.remove(root.val)
            return fun(root.left,l) or fun(root.right,l)
        self.res=root

        def fun2(root):
            if not root:
                return
            if fun(root,l[:]):
                self.res=root
                fun2(root.left)
                fun2(root.right)
            return
        fun2(root)
        return self.res


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #有3种情况(这种递归是重下往上走的，可以好好思考下)：
        #1.如果左边不含有p或者q，则最大公共祖先一定在右边
        #2.如果右边不含有p或者q，则最大公共祖先一定在左边
        #3.左右都有，则最大公共祖先是本节点
        def fun(root,p,q):
            if not root or root==p or root==q:
                return root
            left=fun(root.left,p,q)
            right=fun(root.right,p,q)
            if not left:
                return right
            if not right:
                return left
            return root

        return fun(root,p,q)


