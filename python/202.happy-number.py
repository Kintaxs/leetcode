class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        s = set()

        while(True):
            if(n==1 and n not in s):
                return True
            elif(n in s):
                return False
            s.add(n)
            n = self.squareSum(n)
        
    def squareSum(self, n):
        
        sum = 0

        while(n/10 >= 1):
            sum += pow(n%10, 2)
            n /= 10
        sum += pow(n, 2)

        return sum

