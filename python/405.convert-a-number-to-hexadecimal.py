class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if(num == 0): 
            return '0'
        elif(num < 0): 
            num += 2 ** 32

        d = {'0':'0', '1':'1', '2':'2', '3':'3', '4':'4', '5':'5', '6':'6', '7':'7', '8':'8', "9":'9', '10':'a', '11':'b', '12':'c', '13':'d', '14':'e', '15':'f'}

        l = list()
        res = list()

        for i in range(8):
            l.append(pow(16, i)) 

        l = l[::-1]

        for i in l:
            if num >= i:
                q = num / i 
                num = num % i 
                print('q:', q, d[str(q)])
                res.append(d[str(q)])
            elif num == 0 or (num < i and len(res) > 0):
                res.append(d['0'])            

        return "".join(res)

        
