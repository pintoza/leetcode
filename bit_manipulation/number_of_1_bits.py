"""
Write a function that takes the binary representation of an unsigned integer and returns the number of '1'
bits it has (also known as the Hamming weight).
"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        while n:
            n &= (n - 1)
            count += 1

        return count