# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        arr=[]
        while head:
            arr.append(head.val)
            head=head.next
        def fun(arr):
            if not arr:
                return
            size=len(arr)
            mid=size//2
            root=TreeNode(arr[mid])
            root.left=fun(arr[:mid])
            root.right=fun(arr[mid+1:])
            return root
        return fun(arr)