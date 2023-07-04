# https://leetcode.com/problems/same-tree/description/
# Given the roots of two binary trees p and q, write a function to check if they are the same or not.
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def is_same(x, y):
            if x is None:
                return y is None
            if y is None:
                return x is None
            return (x.val == y.val) and is_same(x.left, y.left) and is_same(x.right, y.right)
        return is_same(p, q)
