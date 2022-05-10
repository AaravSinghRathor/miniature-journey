# Given two strings s and t, return true if they are equal when both are typed into empty text editors.
# '#' means a backspace character.
#
# Note that after backspacing an empty text, the text will continue empty.

# Example
# Input: s = "ab#c", t = "ad#c"
# Output: true
# Explanation: Both s and t become "ac".

from collections import deque

class Solution:

    def get_string_after_rem_backspace_chars(self, string_1):

        stack = deque()

        for c in string_1:

            if c == '#':
                if not stack:
                    continue
                else:
                    stack.pop()
            else:
                stack.append(c)

        return stack

    def backspaceCompare(self, s: str, t: str) -> bool:

        return self.get_string_after_rem_backspace_chars(s) == self.get_string_after_rem_backspace_chars(t)


s = "a#c"
t = "b"
print(Solution().backspaceCompare(s, t))