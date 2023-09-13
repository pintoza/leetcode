"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters.
No two characters may map to the same character, but a character may map to itself.
"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        s_string = {}
        t_string = {}

        for i in range(len(s)):
            if t[i] not in t_string and s[i] not in s_string:
                s_string[s[i]] = t[i]
                t_string[t[i]] = s[i]
            elif s_string.get(s[i]) != t[i] or t_string.get(t[i]) != s[i]:
                return False

        return True
