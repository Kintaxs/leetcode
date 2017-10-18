class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        s = set()
        
        for i in nums:
            s.add(i)

        if(len(nums) == len(s)):
            return False
        else:
            return True
