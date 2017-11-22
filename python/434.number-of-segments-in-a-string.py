class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """

        l = s.split(' ')

        count = 0

        for i in l:
            if i != "":
                count += 1

        return count
