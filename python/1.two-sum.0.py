class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dictx = {}

        for index,val in enumerate(nums):
            rest = target - val
            if rest in dictx:
                return [index,dictx[rest]]
            else:
                dictx[val] = index
