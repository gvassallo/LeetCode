# The count-and-say sequence is the sequence of integers with the first five terms as
# following:
#
# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
# Given an integer n, generate the nth term of the count-and-say sequence.
#
# Note: Each term of the sequence of integers will be represented as a string.


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        def helper(s):
            result = [] 
            num = s[0] 
            cnt = 1 
            for i in range(1, len(string)): 
                if string[i] == num: 
                    cnt +=1 
                else: 
                    result.append(str(cnt))
                    result.append(num) 
                    num = string[i] 
                    cnt = 1 
            result.append(str(cnt))
            result.append(num) 
            return ''.join(result) 

        string = '1'
        for i in range(1, n): 
            string = helper(string) 
        return string 


if __name__ == "__main__": 
    for i in range(1, 6):
        print Solution().countAndSay(i)
