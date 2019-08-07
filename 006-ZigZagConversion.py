# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like
# this: (you may want to display this pattern in a fixed font for better legibility)
#
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
#
# Write the code that will take a string and make this conversion given a number of rows:
#
# string convert(string s, int numRows);

class Solution:
    def convert(self, s: str, rows: int) -> str:
        if len(s) == 1 or rows == 1:
            return s
        res = [""] * rows
        index, step = 0, 1
        for x in s:
            res[index] += x
            if index == 0:
                step = 1
            elif index == rows - 1:
                step = -1
            index += step
            print(res)
        return "".join(res)
