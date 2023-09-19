"""
Given an integer array nums where the elements are sorted in ascending order, convert it to a
height-balanced
 binary search tree.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # Base case: If the list is empty, return None.
        if not nums:
            return None

        # Find the middle index of the list.
        mid = len(nums) // 2

        # Create a new tree node with the middle value of the list.
        root = TreeNode(nums[mid])

        # Set the left child of the root to the result of the first half of the list.
        root.left = self.sortedArrayToBST(nums[:mid])

        # Set the right child of the root to the result of the second half of the list.
        root.right = self.sortedArrayToBST(nums[mid + 1:])

        return root
