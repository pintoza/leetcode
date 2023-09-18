"""
Given the root of a binary tree, return the average value of the nodes on each level
in the form of an array. Answers within 10-5 of the actual answer will be accepted.

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        levelData = defaultdict(lambda: {'nodeCount': 0, 'nodeValueSum': 0})

        def traverseTree(node, level=0):
            if not node:
                return
            levelData[level]['nodeCount'] += 1
            levelData[level]['nodeValueSum'] += node.val
            traverseTree(node.left, level + 1)
            traverseTree(node.right, level + 1)

        traverseTree(root)

        averages = []

        for data in levelData.values():
            averageValue = data['nodeValueSum'] / data['nodeCount']
            averages.append(averageValue)

        return averages
