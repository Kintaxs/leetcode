class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        
        if(b == 0):
            return a if a <= 0x7FFFFFFF else ~(a ^ 0xFFFFFFFF)

        s = (a ^ b) & 0xFFFFFFFF
        carry = ((a & b) << 1) & 0xFFFFFFFF

        return self.getSum(s, carry)
