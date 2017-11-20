class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        minimum = 2 ** 32
        res = 0

        for i in nums:
            minimum = min(minimum, i)

        for i in nums:
            res += (i - minimum)

        return res



