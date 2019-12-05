# Count the number of segments in a string, where a segment is defined to be a contiguous
# sequence of non-space characters.
#
# Please note that the string does not contain any non-printable characters.

class Solution:
    def countSegments(self, s: str) -> int:
        result = 0
        prev_space = True
        for x in s:
            if x != " ":
                if prev_space:
                    result += 1
                prev_space = False
            else:
                prev_space = True
        return result
