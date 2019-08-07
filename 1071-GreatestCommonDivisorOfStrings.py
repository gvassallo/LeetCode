# For strings S and T, we say "T divides S" if and only if S = T + ... + T  (T concatenated with itself 1 or more times)
# Return the largest string X such that X divides str1 and X divides str2.

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) == len(str2): return str1 if str1 == str2 else ""
        elif len(str1) < len(str2): return self.gcdOfStrings(str2, str1)
        elif str1[:len(str2)] == str2: return self.gcdOfStrings(str1[len(str2):], str2)
        return ""
