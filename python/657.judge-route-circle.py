class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        
        sum1 = 0
        sum2 = 0

        for i in moves:
            if i == 'U':
                sum1 += 1
            elif i == 'D':
                sum1 -= 1
            elif i == 'L':
                sum2 += 1
            elif i == 'R':
                sum2 -= 1

        if sum1 == 0 and sum2 == 0:
            return True
        else:
            return False
