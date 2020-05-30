class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1:
    def isSymmetric(self, root: TreeNode) -> bool:
        def helper(root1,root2):
            if not root1 and not root2:
                return True
            elif not root1 or not root2:
                return False
            elif root1.val==root2.val:
                return helper(root1.left,root2.right) and helper(root1.right,root2.left)
        return helper(root,root)

class Solution2:
    def isSymmetric(self, root: TreeNode) -> bool:
        head=root
        def fun(root1,root2):
            if not root1 or  not root2:
                if not root1 and not root2:
                    return True
                else:
                    return False
            if root1.val==root2.val:
                return fun(root1.left,root2.right) and fun(root1.right,root2.left)
            return False
        return fun(head,root)
from collections import deque
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        #尝试迭代解法
        head=root
        stack=deque()
        stack.append((root,head))
        while stack:
            tmp1,tmp2=stack.popleft()
            if not tmp1 or not tmp2:
                if not tmp1 and not tmp2:
                    continue
                else:
                    return False
            if tmp1.val==tmp2.val:
                stack.append((tmp1.left,tmp2.right))
                stack.append((tmp1.right,tmp2.left))
            else:
                return False
        return True


