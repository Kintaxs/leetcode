class Solution(object):
    def reverseWords(self, s):
	""" 
	:type s: str
	:rtype: str
	"""
	
	l = s.split(' ')
	res = list()

	for i in l:
	    tmp = list(i)
	    tmp = tmp[::-1]
	    res.append("".join(tmp) + ' ')

	return "".join(res).rstrip(" ")


