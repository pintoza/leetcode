"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {
            "(": 1,
            ")": 2,
            "{": 3,
            "}": 4,
            "[": 5,
            "]": 6
        }

        if mapping[s[0]] % 2 == 0:
            return False

        if mapping[s[-1]] % 2 != 0:
            return False

        if len(s) % 2 != 0:
            return False

        # initialize stack
        stack = []

        for i, char in enumerate(s):
            mapped_value = mapping.get(char, None)

            # If opening element, push it and its index onto the stack
            if mapped_value % 2 == 1:
                stack.append((mapped_value, i))

            # If closing element, pop the last opening element from the stack and check conditions
            else:
                if not stack:
                    return False

                last_open_val, last_open_index = stack.pop()

                if last_open_val + 1 != mapped_value:
                    return False

                if (i - last_open_index) % 2 == 0:
                    return False

        return True if not stack else False
