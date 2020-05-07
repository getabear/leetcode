class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        #暴力递归，通过
        def fun(s,t):
            if not s and not t:
                return True
            if not s or not t:
                return False
            if s.val==t.val:
                if fun(s.left,t.left) and fun(s.right,t.right):
                    return True
            return False

        def fun2(s,t):
            if not s:
                return False
            if s.val==t.val:
                if fun(s,t):
                    return True
            return fun2(s.left,t) or fun2(s.right,t)


        return fun2(s,t)

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def fun(root,res):
            if not root:
                return
            fun(root.left,res)
            res.append(root.val)
            fun(root.right,res)

        s1=[]
        t1=[]
        fun(s,s1)
        fun(t,t1)
        i,j=1,-1
        next=[-1]
        while i<len(t1):
            if j==-1 or t1[i]==t1[j]:
                i += 1
                j += 1
                next.append(j)
            else:
                j=next[j]
        i,j=0,0
        while i<len(s1) and j<len(t1):
            if j==-1 or s1[i]==t1[j]:
                i+=1
                j+=1
            else:
                j=next[j]
        if j==len(t1):
            return True
        return False