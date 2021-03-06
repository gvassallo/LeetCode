# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine
# if the input string is valid.
# The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and
# "([)]" are not


class Solution(object):
    def isValid(self, s):
        stack = []
        dict = {"]":"[", "}":"{", ")":"("}
        for char in s:
            if char in dict.values():
                stack.append(char)
            elif char in dict.keys():
                if stack == [] or dict[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []


if __name__ == "__main__": 
    assert Solution().isValid('()[]{}') == True
    assert Solution().isValid('([]{})') == True
    assert Solution().isValid('([]{}') == False

