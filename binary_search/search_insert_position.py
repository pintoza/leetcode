"""
Given a sorted array of distinct integers and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
"""
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        if not nums:
            return 0

        for i, num in enumerate(nums):
            if num >= target:
                return i

        return len(nums)
