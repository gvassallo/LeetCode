# Given an array of characters, compress it in-place.
# The length after compression must always be smaller than or equal to the original array.
# Every element of the array should be a character (not int) of length 1.
# After you are done modifying the input array in-place, return the new length of the array.

class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        cnt = 1
        prev_ch = chars[0]

        for j in range(1, len(chars) + 1):
            if j == len(chars) or chars[j] != prev_ch:
                chars[i] = prev_ch
                if cnt > 1:
                    for n in list(str(cnt)):
                        i += 1
                        chars[i] = n
                if j < len(chars):
                    prev_ch = chars[j]
                i += 1
                cnt = 1
            else:
                cnt += 1
        return i
