from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# deque
# 数据类型来自于
# collections 模块，支持从头和尾部的常数时间a ppend/pop 操作。若使用 Python 的 list，通过 list.pop(0) 去除头部会消耗 {O}(n)O(n) 的时间。
#以后可以使用deque
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        queue=[]
        ret=[]
        if root:
            queue.append([root,0])
        else:
            return []
        while queue:
            tp,level=queue.pop(0)
            try:
                ret[level].append(tp.val)
            except:
                ret.append([])
                ret[level].append(tp.val)
            if tp.left:
                queue.append([tp.left,level+1])
            if tp.right:
                queue.append([tp.right,level+1])
        res=[]
        for i in ret:
            res.append(i[-1])
        return res