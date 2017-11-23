class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
	medal = ["Gold Medal", "Silver Medal", "Bronze Medal"]
	nums_sort = sorted(nums, reverse=True)
	res = nums[::]

        start = 3 if len(nums)>3 else len(nums)

	for i in range(start):
	    res[nums.index(nums_sort[i])] = medal[i]
	for i in range(start, len(nums_sort)):
	    res[nums.index(nums_sort[i])] = str(i + 1)
	return res 

