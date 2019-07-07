# Given a string, find the length of the longest substring without repeating characters.
# Examples:
# Given "abcabcbb", the answer is "abc", which the length is 3.
# Given "bbbbb", the answer is "b", with the length of 1.
# Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be
# a substring, "pwke" is a subsequence and not a substring.


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter = 0 
        chars = {} 
        max = 0 
        for i in range(len(s)): 
            if s[i] not in chars: 
                counter += 1 
                chars[s[i]] = i
            else: 
                counter -= i - chars[s[i]] + 1  
                chars[s[i]] = i
            if counter > max: 
                max = counter 
        return max


if __name__ == "__main__": 
    s = "abcabcbb" 
    print Solution().lengthOfLongestSubstring(s) 
