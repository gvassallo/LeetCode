# Given an array of strings, group anagrams together.
# For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"], 
# Return:
# [
#  ["ate", "eat","tea"],
#  ["nat","tan"],
#  ["bat"]
# ]


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams = {} 
        for s in strs: 
            sorted_s = "".join(sorted(list(s))) 
            if sorted_s not in anagrams: 
                anagrams[sorted_s] = [s] 
            else: 
                anagrams[sorted_s].append(s) 
        result = [] 
        for key in anagrams: 
            result.append(anagrams[key]) 
        return result


if __name__ == "__main__": 
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print Solution().groupAnagrams(strs)
