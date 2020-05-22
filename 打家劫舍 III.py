class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
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
    def rob(self, root: TreeNode) -> int:
        def fun(root):
            if not root:
                return [0,0]   #当前节点参与的钱，当前节点不参与的钱
            left=fun(root.left)
            right=fun(root.right)
            return [root.val+left[1]+right[1],max(left)+max(right)]
        return max(fun(root))

root=creat_er([1,2,3,None,4,None,5])
a=Solution()
print(a.rob(root))
