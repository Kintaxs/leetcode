class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        size = 0

        for i in nums:
            if (i != val):
                nums[size] = i
                size += 1
        return size
