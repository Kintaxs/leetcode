class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        l = s.split()

        if(len(l) <= 0):
            return 0
        else:
            res = len(l[len(l)-1])
            return res
