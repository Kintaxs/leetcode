class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        nums.reverse()

        k %= len(nums)

        nums[:k] = nums[:k][::-1]
        nums[k:] = nums[k:][::-1]
