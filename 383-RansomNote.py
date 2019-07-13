# Given an arbitrary ransom note string and another string containing letters from all the
# magazines, write a function that will return true if the ransom note can be constructed
# from the magazines ; otherwise, it will return false.
#
# Each letter in the magazine string can only be used once in your ransom note.
#
# Note:
# You may assume that both strings contain only lowercase letters.

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq_m = [0 for _ in range(26)]

        for m in magazine:
            freq_m[ord(m) - ord("a")] += 1

        for r in ransomNote:
            if freq_m[ord(r) - ord("a")] == 0:
                return False
            else:
                freq_m[ord(r) - ord("a")] -= 1
        return True
