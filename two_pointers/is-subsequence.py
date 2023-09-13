"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none)
of the characters without disturbing the relative positions of the remaining characters.
(i.e., "ace" is a subsequence of "abcde" while "aec" is not).
"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_index = 0

        # Iterate through the characters in the string t
        for char in t:
            # If the current character in t matches the current character in s, move to the next character in s
            if s_index < len(s) and char == s[s_index]:
                s_index += 1

        # If s_index is equal to the length of s, all characters in s were found in t in the correct order
        return s_index == len(s)






