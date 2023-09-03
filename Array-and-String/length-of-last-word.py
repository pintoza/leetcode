"""
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal
substring
 consisting of non-space characters only.
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        if len(s) == 1:
            return 1

        length = 0

        j = -1

        while s[j].isspace():
            j -= 1

        while -j <= len(s) and not s[j].isspace():
            length += 1
            j -= 1

        return length
