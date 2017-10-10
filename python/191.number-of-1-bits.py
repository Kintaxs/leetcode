class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """

        count = 0

        for i in range(32, -1, -1):
            pow_value = pow(2, i)
            if(n >= pow_value):
                n -= pow_value
                count += 1

        return count

