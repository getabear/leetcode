from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        def build(n):
            if n==1:
                return [TreeNode(0)]
            if n%2==0:
                return []
            left_num=1
            res=[]
            while left_num<n:
                left=build(left_num)
                right=build(n-left_num-1)
                for l in range(len(left)):
                    for r in range(len(right)):
                        root=TreeNode(0)
                        root.left=left[l]
                        root.right=right[r]
                        res.append(root)
                left_num+=2
            return res
        return build(N)

a=Solution()
N=7
print(a.allPossibleFBT(N))