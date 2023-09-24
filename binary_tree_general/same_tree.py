"""
Given the roots of two binary 05_trees p and q, write a function to check if they are the same or not.

Two binary 05_trees are considered the same if they are structurally identical, and the nodes have the same value.
"""


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return p is q
