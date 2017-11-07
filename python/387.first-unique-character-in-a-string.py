class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """

        d = dict()

        for i in s:
            if d.has_key(i):
                d[i] += 1
            else:
                d[i] = 1

        for i in range(len(s)):
            if(d[s[i]] == 1):
                return i

        return -1
        
