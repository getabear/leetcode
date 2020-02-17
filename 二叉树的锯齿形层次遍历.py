from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    #思路一:层次遍历后再进行翻转
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        stack=[]
        if root:
            stack=[(root,0)]
        ret=[]
        while stack:
            tp,index=stack.pop(0)
            try:
                ret[index].append(tp.val)
            except:
                ret.append([])
                ret[index].append(tp.val)
            if  tp.left:
                stack.append((tp.left,index+1))
            if  tp.right:
                stack.append((tp.right,index+1))
        length=len(ret)
        for i in range(length):
            if i&0x1:      #先从左到右,后从右到左
                ret[i]=ret[i][::-1]
        return ret
# 思路二:双端队列,以后做(可能永远不会做哈哈哈哈)