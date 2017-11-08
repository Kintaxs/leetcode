class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        d = dict()

        for i in s:
            if d.has_key(i):
                d[i] += 1
            else:
                d[i] = 1

        for i in t:
            if d.has_key(i):
                if(d[i] == 0):
                    return i
                d[i] -= 1
            else:
                return i
