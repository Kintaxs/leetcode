class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        nums = []

        for i in s:
            nums.append(ord(i) - ord('A') + 1)

        res = 0
        nums_size = len(nums)

        for idx, data in enumerate(nums, 1):
            res += data * (pow(26, nums_size-idx))

        return res
