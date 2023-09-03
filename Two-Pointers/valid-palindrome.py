"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:

        # Create a dictionary to map each letter to a number
        letter_to_number = {letter: index + 1 for index, letter in enumerate('abcdefghijklmnopqrstuvwxyz0123456789')}

        # Use list comprehension to filter out non-alphabetic characters
        s = (''.join([char for char in s if char.lower() in letter_to_number])).lower()

        s_len_half = len(s) // 2

        i = 0
        j = -1
        k = 0

        for char in range(s_len_half):
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                k += 1

        if k != 0:
            return False
        else:
            return True


