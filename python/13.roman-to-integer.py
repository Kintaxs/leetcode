class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        # I:1 V:5 X:10 L:50 C:100 D:500 M:1000

        romantoint_list = [1, 5, 10, 50, 100, 500, 1000]
        roman_list = []
        sum = 0

        for i in s:
            if(i == 'I'):
                roman_list.append(0)
            elif(i == 'V'):
                roman_list.append(1)
            elif(i == 'X'):
                roman_list.append(2)
            elif(i == 'L'):
                roman_list.append(3)
            elif(i == 'C'):
                roman_list.append(4)
            elif(i == 'D'):
                roman_list.append(5)
            elif(i == 'M'):
                roman_list.append(6)

        for i in xrange(0, len(s)-1):
            if(roman_list[i] < roman_list[i+1]):
                sum -= romantoint_list[roman_list[i]]
            else:
                sum += romantoint_list[roman_list[i]]

        sum += romantoint_list[roman_list[len(s)-1]]

        return sum


