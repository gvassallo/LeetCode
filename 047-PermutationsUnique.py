class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def helper(prefix, remaining): 
            if remaining == 0: 
                result.append(prefix) 
                return 
            for c in freq_table: 
                count = freq_table[c] 
                if count > 0: 
                    freq_table[c] -= 1 
                    helper(prefix + [c], remaining - 1)
                    freq_table[c] = count 
            return 
        freq_table = self.build_freq_table(nums) 
        result = [] 
        helper([], len(nums)) 
        return result 
        
    def build_freq_table(self, nums): 
        freq_table = {} 
        for n in nums: 
            if n not in freq_table: 
                freq_table[n] = 1
            else: 
                freq_table[n] += 1
        return freq_table 


if __name__ == "__main__": 
    nums = [1, 1, 2] 
    print Solution().permuteUnique(nums) 
