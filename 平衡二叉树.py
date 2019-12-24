class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def creat_er(nums):
    def fun(nums,node):
        if len(nums)==0 or node==None:
            return None
        if  len(nums)>0:
            if nums[0]!=None:
                node.left=TreeNode(nums[0])
        if len(nums)>1:
            if nums[1]!=None:
                node.right=TreeNode(nums[1])
        fun(nums[2:],node.left)
        fun(nums[4:],node.right)

    if len(nums)<1:
        return None
    node=TreeNode(nums[0])
    fun(nums[1:],node)
    return node

class Solution1:
    #没写完...
    def isBalanced(self, root: TreeNode) -> bool:
        self.left=0
        self.right=0
        def fun(root: TreeNode):
            if not root:
                return 0
            left=1+fun(root.left)
            right=1+fun(root.right)
            return max(left,right)

        n=fun(root)
        return n

class Solution:
    #别人的题解
    def isBalanced(self, root: TreeNode) -> bool:
        return self.depth(root) != -1

    def depth(self, root):
        if not root: return 0
        left = self.depth(root.left)
        if left == -1: return -1
        right = self.depth(root.right)
        if right == -1: return -1
        return max(left, right) + 1 if abs(left - right) < 2 else -1

a=Solution()
nums=[3,9,20,None,None,15,7]
node=creat_er(nums)
print(a.isBalanced(node))