# Write a function that takes a string as input and reverse only the vowels of a string.

class Solution:
    def reverseVowels(self, s: str) -> str:
        VOWELS = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        s = list(s)
        i, j = 0, len(s) - 1

        while i < j:
            while s[i] not in VOWELS and i < j: i += 1
            while s[j] not in VOWELS and j > i: j -= 1
            if s[i] in VOWELS and s[j] in VOWELS:
                s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        return "".join(s)
