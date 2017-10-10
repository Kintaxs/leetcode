class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):

        res = 0

        for i in range(31, -1, -1):
            pow_value = pow(2, i)

            if(n >= pow_value):
                n -= pow_value
                res += pow(2, 31-i)
        return res
        
