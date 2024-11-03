# Leetcode Problem 110: Balanced Binary Tree
# Given a binary tree, determine if it is height-balanced
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check(node):
            if not node:
                return 0
            lh = check(node.left)
            if lh == -1:
                return -1
            rh = check(node.right)
            if rh == -1:
                return -1
            if abs(lh-rh) > 1:
                return -1
            return 1 + max(lh, rh)
        return check(root) != -1
            
        
