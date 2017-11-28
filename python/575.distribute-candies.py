class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """

        num_candy = len(candies)
        d = dict()

        for i in candies:
            if d.has_key(i) == True:
                d[i] += 1
            else:
                d[i] = 1

        for i in range(num_candy/2, 0, -1):
            if(len(d) >= i):
                return i
