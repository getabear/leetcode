class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode):
        ret=[]
        if not root:
            return ret

        def helper(node,level):
            if len(ret)==level:
                ret.append([])    #到新的一层,添加新列表

            ret[level].append(node.val)

            if node.left:
                helper(node.left,level+1)
            if node.right:
                helper(node.right,level+1)

        helper(root,0)
        return  ret

