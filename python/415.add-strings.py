class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        
        n1 = self.getNum(num1)
        n2 = self.getNum(num2)

        return str(n1 + n2)

    def getNum(self, strs):

        l = list()

        for i in strs:
            l.append(i)

        l = l[::-1]

        num = 0

        for i, data in enumerate(l):
            num += int(data) * pow(10, i)

        return num

