class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pval=min(p.val,q.val)
        qval=max(p.val,q.val)
        while root:
            if pval<=root.val<=qval:
                return root
            if pval<root.val:
                root=root.left
            else:
                root=root.right
        return None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pval=p.val
        qval=q.val

        def fun(root):
            if pval<root.val and qval<root.val:
                return fun(root.left)
            elif pval>root.val and qval>root.val:
                return fun(root.right)
            else:
                return root
        return fun(root)