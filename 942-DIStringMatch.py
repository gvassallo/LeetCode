# Given a string S that only contains "I" (increase) or "D" (decrease), let N = S.length.
#
# Return any permutation A of [0, 1, ..., N] such that for all i = 0, ..., N-1:
#
# If S[i] == "I", then A[i] < A[i+1]
# If S[i] == "D", then A[i] > A[i+1]


class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        result = []
        max_n = len(S)
        min_n = 0
        for i in range(len(S)):
            if S[i] == "D":
                result.append(max_n)
                max_n -= 1
            else:
                result.append(min_n)
                min_n += 1
        result.append(max_n if S[-1] == "D" else min_n)
        return result
