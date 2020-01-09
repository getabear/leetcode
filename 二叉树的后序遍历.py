from typing import List
from git import er

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    #提交通过,击败6.63%的用户,迭代方法下次来
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        self.ret=[]
        def fun(root: TreeNode):
            if not root:
                return
            fun(root.left)
            fun(root.right)
            self.ret.append(root.val)
            return

        fun(root)
        return self.ret

class Solution1:
    #迭代方案,提交后通过,击败15%的用户
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        self.ret=[]
        if not root:
            return []
        stack=[[root,1]]
        head=root.left
        while head or stack:
            while head:
                stack.append([head,1])
                head=head.left
            while stack and stack[-1][1]==2: #这里注意需要把所有的访问了两次的节点取出
                tp=stack.pop()
                self.ret.append(tp[0].val)
            if stack:
                stack[-1][1]+=1
                head,time=stack[-1]
                head=head.right

        return self.ret



b=er()
a=Solution1()
nums=[1,None,2,3]
head=b.creat_er(nums)
print(a.postorderTraversal(head))