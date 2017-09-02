class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        temp = abs(x)

        if(temp == 0):
            return True
        elif(x < 0):
            return False

        listx = []
        while(temp>0):
            listx.append(temp%10)
            temp = temp/10

        if(len(listx)%2 == 0):
            middle = len(listx)/2
        else:
            middle = (len(listx)-1)/2

        for i in xrange(0,middle):
            if(listx[i] != listx[len(listx)-1-i]):
                return False
        return True
