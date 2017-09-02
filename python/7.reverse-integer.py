class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        if(x == 0):
            return 0
        elif(x > (2**31-1) or x < (2**31 * -1)):
            return 0

        temp = abs(x)
        listx = []
        ans = 0

        while(temp > 0):
            listx.append(temp % 10)
            temp = temp / 10

        for i in xrange(0, len(listx)):
            ans = ans*10 + listx[i]

        if(ans > (2**31-1) or ans < (2**31 * -1)):
            return 0

        if(x < 0):
            return ans*-1
        else:
            return ans

