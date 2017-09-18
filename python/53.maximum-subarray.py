class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        local = list()
        local.append(nums[0])
        res = local[0]

        for i in xrange(1, len(nums)):
            local.append(max(nums[i], nums[i]+local[i-1]))
            res = max(res, local[i])

        return res

