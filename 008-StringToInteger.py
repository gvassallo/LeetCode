# Implement atoi which converts a string to an integer.

class Solution:
    def myAtoi(self, str: str) -> int:
        if len(str) == 0:
            return 0
        i = 0
        while str[i] == " " and i < len(str) -1:
            i += 1
        if i == len(str):
            return 0
        sign = 1
        if str[i] == "+":
            i += 1
        elif str[i] == "-":
            sign = -1
            i += 1
        num = 0
        while i < len(str) and str[i].isdigit():
            num = num * 10 + int(str[i])
            i += 1
        if sign == 1:
            return min(2**31 - 1, num)
        else:
            return max(-2**31, -num)
