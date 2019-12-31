from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None

        mid=len(nums)//2
        node=TreeNode(nums[mid])
        left=nums[:mid]
        right=nums[mid+1:]

        node.left=self.sortedArrayToBST(left)
        node.right=self.sortedArrayToBST(right)
        return node
