"""
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
"""

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return self.isMirror(root.left, root.right)

    def isMirror(self, node1, node2):
        if node1 is None and node2 is None:
            return True
        if node1 and node2 and node1.val == node2.val:
            return self.isMirror(node1.left, node2.right) and self.isMirror(node1.right, node2.left)
        return False
