class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        d = dict()

        for idx, data in enumerate(nums):
            x = d.get(data)
            if(x != None):
                if(abs(x - idx) <= k):
                    return True
            d[data] = idx
        return False
