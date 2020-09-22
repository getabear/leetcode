class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        self.min_camera = 0
        def dfs(root):
            if not root:    #如果当前节点为空，则父节点不需要监控，返回1
                return 1
            ret1=dfs(root.left)
            ret2=dfs(root.right)
            if ret1 and ret2: #如果两个子节点都不需要监控，返回较大的值
                return max(ret1,ret2)-1
            if ((root.left and root.left.val==0) or (root.right and root.right.val==0)):
                root.val = 1
                self.min_camera += 1
                return 2    #设置了监控后，父节点不需要额外监控
            return 0
        if not root:   #特殊情况
            return 0
        if (not root.left) and (not root.right): #特殊情况
            return 1
        dfs(root)
        if root.val != 1 and (root.left or root.right):   #退出递归后，如果根节点没被安装监控
            #如果根节点的子节点有一个安装了监控
            if (root.left and root.left.val == 1) or (root.right and root.right.val ==1):
                return self.min_camera
            #根节点的子节点都没安装监控，需要在根节点安装监控
            else:
                return self.min_camera+1
        # 根节点安装了监控
        return self.min_camera


