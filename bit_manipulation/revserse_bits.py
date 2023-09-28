"""
Reverse bits of a given 32 bits unsigned integer.
"""


class Solution:
    def reverseBits(self, n: int) -> int:
        reversedBits = 0

        for _ in range(32):
            reversedBits = (reversedBits << 1) | (n & 1)
            n >>= 1

        return reversedBits
