from collections import deque

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        queue=deque()
        res=[]
        queue.append(root)
        while queue:
            root=queue.popleft()
            if root:
                res.append(root.val)
                queue.append(root.left)
                queue.append(root.right)
            else:
                res.append(None)
        return str(res)


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        l=[]
        s=""
        for i in data:
            if i=="[":
                continue
            elif i==',' or i==']':
                if s==" None":
                    l.append(None)
                else:
                    l.append(int(s))
                s=""
            else:
                s+=i
        queue=deque()
        head=TreeNode(l[0])
        queue.append(head)
        index=1
        while queue and index<len(l):
            root=queue.popleft()
            if l[index]!=None:
                root.left=TreeNode(l[index])
                queue.append(root.left)
            if l[index+1]!=None:
                root.right=TreeNode(l[index+1])
                queue.append(root.right)
            index+=2
        return head
data=[1,2,3,None,None,4,5]
print(str(data))
a=Codec()
