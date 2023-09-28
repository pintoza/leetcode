"""Given two binary strings a and b, return their sum as a binary string.

"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        carry = 0
        i, j = len(a) - 1, len(b) - 1

        while i >= 0 or j >= 0:
            current_sum = carry
            if i >= 0:
                current_sum += int(a[i])
                i -= 1
            if j >= 0:
                current_sum += int(b[j])
                j -= 1

            carry = current_sum // 2
            result.append(str(current_sum % 2))

        if carry:
            result.append(str(carry))

        return "".join(result[::-1])