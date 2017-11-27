# Given a collection of intervals, merge all overlapping intervals.
#
# For example,
# Given [1,3],[2,6],[8,10],[15,18],
# return [1,6],[8,10],[15,18]


class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __repr__(self): 
        return '['+ str(self.start) + ',' + str(self.end) + ']'


class Solution(object):
    def merge(self, arr):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(arr) == 0:
            return arr
        arr = sorted(arr, key=lambda x: x.start) 
        res = []
        curr = arr[0]
        for i in range(1, len(arr)): 
            if curr.end >= arr[i].start: 
                curr.end = max(curr.end, arr[i].end)
            else: 
                res.append(curr)
                curr = arr[i]
        res.append(curr)
        return res 


if __name__ == "__main__": 
     arr = [Interval(1, 3), Interval(2, 6), Interval(8, 10), Interval(15, 18)] 
     print Solution().merge(arr)  
