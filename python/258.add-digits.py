class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        while(num >= 10):
            num = self.transform(num)

        return num

    def transform(self, n):
        
        sum = 0

        while(n >= 10):
            sum = sum + n % 10
            n /= 10

        sum += n
        
        return sum
