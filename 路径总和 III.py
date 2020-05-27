class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        self.res=0
        def dfs(root,s):
            if not root:
                return
            s+=root.val
            if s==sum:
                self.res+=1
            dfs(root.left,s)
            dfs(root.right,s)
            return
        def fun(root):
            if not root:
                return
            dfs(root,0)
            fun(root.left)
            fun(root.right)
            return
        fun(root)
        return self.res

def creat_er(nums):  #宽度优先遍历利用数组构造二叉树,nums是构造二叉树的数组
    if not nums:
        return
    root=TreeNode(nums[0])
    queue=[root]
    length=len(nums)
    index=1
    while(queue):
        newroot=queue.pop(0)
        if index<length and newroot:
            if nums[index]!=None:
                newroot.left=TreeNode(nums[index])
            else:
                newroot.left=None
            index+=1
            queue.append(newroot.left)
        if index<length and newroot:
            if nums[index]!=None:
                newroot.right=TreeNode(nums[index])
            else:
                newroot.right=None
            index+=1
            queue.append(newroot.right)

    return root

root=creat_er([10,5,-3,3,2,None,11,3,-2,None,1])
a=Solution()
print(a.pathSum(root,8))