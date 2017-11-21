class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        complement = list()

        for i in range(1, 32):
            complement.append(pow(2, i) - 1)

        for i in complement:
            if num <= i:
                return i - num
