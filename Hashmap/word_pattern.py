"""
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.
"""

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        s_words = s.split()

        if len(pattern) != len(s_words):
            return False

        for i in range(len(pattern)):
            for j in range(len(pattern)):
                if pattern[i] == pattern[j]:
                    if s_words[i] != s_words[j]:
                        return False
                if pattern[i] != pattern[j]:
                    if s_words[i] == s_words[j]:
                        return False

        return True