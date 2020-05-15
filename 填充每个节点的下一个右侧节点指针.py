class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        ret=[]
        def fun(root,level):
            if not root:
                return
            try:
                ret[level].append(root)
            except:
                ret.append([])
                ret[level].append(root)
            fun(root.left,level+1)
            fun(root.right,level+1)
            return
        fun(root,0)
        for i in ret:
            for j in range(len(i)):
                if j==len(i)-1:
                    i[j].next=None
                else:
                    i[j].next=i[j+1]
        return root
