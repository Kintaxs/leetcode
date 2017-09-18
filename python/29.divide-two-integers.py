class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """

        MAX_INT = 2**31 -1

        n_dividend = True if (dividend < 0) else False
        n_divisor = True if (divisor < 0) else False

        dividend = abs(dividend)
        divisor = abs(divisor)

        res = 0

        while(dividend >= divisor):

            sum = divisor
            count = 1

            while(dividend >= (sum << 1)):
                sum = sum << 1
                count = count << 1

            dividend -= sum
            res += count

        if(not n_dividend and not n_divisor):
            return min(res, MAX_INT)
        elif(not n_dividend or not n_divisor):
            return min(res*-1, MAX_INT)
        else:
            return min(res, MAX_INT)
