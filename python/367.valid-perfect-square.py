class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """

        MAX_INT = 2147483647

        perfect_square = list()

        index = 1

        while(index * index <= MAX_INT):
            perfect_square.append(index*index)
            index += 1
        
        if num in perfect_square:
            return True
        else:
            return False
