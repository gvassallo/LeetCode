class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        three_maxs = [-sys.maxsize for _ in range(3)]

        for x in nums:
            for i in range(len(three_maxs)):
                if x > three_maxs[i]:
                    three_maxs.pop(2)
                    three_maxs.insert(i, x)
                    break
                if x == three_maxs[i]:
                    break

        if -sys.maxsize in three_maxs:
            return max(three_maxs)

        return three_maxs[2]
