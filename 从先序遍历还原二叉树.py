class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
import collections
class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        if not S: return None
        level = num = 0
        n = len(S)
        dic = collections.defaultdict(list)
        for i, c in enumerate(S):
            if c == '-':
                level +=1
            else:
                num = num * 10 + int(c)
                if i == n-1 or S[i+1] == '-':
                    node = TreeNode(num)
                    dic[level].append(node)
                    if dic[level - 1]:
                        if dic[level-1][-1].left:
                            dic[level-1][-1].right = node
                        else:
                            dic[level-1][-1].left = node
                    level = num = 0
        return dic[0][0]

class Solution1:
    def recoverFromPreorder(self, S: str) -> TreeNode:

        def level(index):
            cnt=0
            while index<len(S):
                if S[index]=='-':
                    cnt+=1
                else:
                    return cnt
                index+=1

        def value(index):
            s=""
            while index<len(S):
                if S[index]=='-':
                    break
                s+=S[index]
                index+=1
            return int(s),len(s)

        def fun(index,deep):
            if index==len(S):
                return  index,None
            dep=level(index)
            if dep<=deep:
                return index,None
            num,n=value(index+dep)
            root=TreeNode(num)
            temp1,child1=fun(index+dep+n,dep)
            root.left=child1
            temp2,child2=fun(temp1,dep)
            root.right=child2
            return temp2,root
        i,head=fun(0,-1)
        return head

class Solution2:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        def level(index):
            cnt=0
            while index<len(S):
                if S[index]=='-':
                    cnt+=1
                else:
                    return cnt
                index+=1
        def value(index):
            s=""
            while index<len(S):
                if S[index]=='-':
                    break
                s+=S[index]
                index+=1
            return int(s),len(s)
        num,n=value(0)
        head=TreeNode(num)
        stack=[(head,0)]
        index=n
        while index<len(S):
            root,deep=stack[-1]
            dep=level(index)
            if dep<=deep:
                stack.pop()
                continue
            num,n=value(index+dep)
            tmp=TreeNode(num)
            if not root.left:
                root.left=tmp
            elif not root.right:
                root.right=tmp
                stack.pop()
            stack.append((tmp,dep))
            index+=dep+n
        return head

S="1-401--349---90--88"
a=Solution2()
a.recoverFromPreorder(S)
