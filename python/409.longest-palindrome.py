class Solution(object):
    def longestPalindrome(self, s):
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

        flag_1 = False
        count_2 = 0

        for i in d:
            if(d[i] % 2 == 1 ):
                flag_1 = True
            count_2 += d[i] / 2

        if(flag_1 == True):
            return count_2 * 2 + 1
        else:
            return count_2 * 2
            

