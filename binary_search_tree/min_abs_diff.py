"""
Given the root of a Binary Search Tree (BST), return the minimum absolute difference
between the values of any two different nodes in the tree.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:

        values = []

        def inOrder(node):
            # Collect node values in ascending order
            if node:
                inOrder(node.left)
                values.append(node.val)
                inOrder(node.right)

        # Collect sorted node values using in-order traversal
        inOrder(root)

        # Calculate differences between adjacent values and return the minimum difference
        min_diff = float('inf')
        for i in range(1, len(values)):
            diff = values[i] - values[i - 1]
            min_diff = min(min_diff, diff)

        return min_diff
