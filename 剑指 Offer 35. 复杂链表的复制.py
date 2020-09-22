class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        ret={}
        def dfs(head):
            if not head:
                return None
            if head in ret:
                return ret[head]
            tmp = Node(head.val,None,None)
            ret[head]=tmp
            tmp.next = dfs(head.next)
            tmp.random = dfs(head.random)
            return ret[head]
        return dfs(head)