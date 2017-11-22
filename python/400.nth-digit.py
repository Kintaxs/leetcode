class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        
	l = list()

	for i in range(10):
	    l.append(9 * pow(10, i)) 

	for i in range(len(l)-1):
	    l[i+1] = l[i+1] * (i+2) + l[i]

	for i in range(len(l)):
	    if( n < l[i]):
		group = i 
		break

        if(group == 0):
            diff = n
            number = diff / (group+1)
            number -= 1
        else:
	    diff = n - l[group-1]
	    number = diff / (group+1)
	digit = diff % (group+1)

	for i in range(pow(10, group), pow(10, group+1)):
	    if(number == 0): 
		res =  self.getDigit(i, digit)
		break
	    number -= 1
        return res


    def getDigit(self, num, digit):

	l = list()

	while(num >= 10):
	    l.append(num%10)
	    num /= 10
	l.append(num)

	l = l[::-1]
	
	if(digit == 0): 
	    return l[-1]
	else:
	    return l[digit-1]

