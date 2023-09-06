"""
You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly.
That is, each element of nums is covered by exactly one of the ranges,
and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b
"""
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        result = []
        count = 0
        i = 0

        while count < len(nums):

            k = i


            while ( i +1) < len(nums) and (nums[i] + 1) == nums[i + 1]:
                i += 1
                count += 1

            if i == k:
                result.append(str(nums[i]))
                i += 1
                count += 1
            else:
                result.append(str(nums[k]) + "->" + str(nums[i]))
                i += 1
                count += 1

        return result
