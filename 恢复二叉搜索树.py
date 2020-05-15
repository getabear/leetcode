class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        ret=[]
        def fun(root):
            if not root:
                return
            fun(root.left)
            ret.append(root)
            fun(root.right)
            return
        fun(root)
        x,y=None,None
        for i in range(len(ret)-1):
            if ret[i].val>ret[i+1].val:
                x=ret[i+1]
                if y==None:
                    y=ret[i]
                else:
                    break
        tmp=x.val
        x.val=y.val
        y.val=tmp
        return
a=Solution()
root=creat_er([3,1,4,None,None,2])
a.recoverTree(root)