class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "0"
        negative = True if num < 0 else False
        num = -1 * num if negative == True else num

        res = list()
        list_base7 = list()
        for i in range(32):
            list_base7.append(pow(7, i))

        list_base7 = list_base7[::-1]

        for i in list_base7:
            if num >= i:
                res.append(str(num / i))
                num %= i
            else:
                if len(res) != 0:
                    res.append('0')

        if negative == False:
            return "".join(res)
        else:
            return '-' + "".join(res)
                



