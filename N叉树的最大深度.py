class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def maxDepth(self, root: 'Node') -> int:

        def fun(root,level):
            if not root.children:
                return level
            ret=0
            for i in root.children:
                ret=max(ret,fun(i,level+1))
            return ret
        if not root:
            return 0
        return fun(root,1)
