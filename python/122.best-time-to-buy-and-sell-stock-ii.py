class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        sum = 0

        for i in range(0, len(prices)-1):
            if(prices[i+1] > prices[i]):
                sum += (prices[i+1] - prices[i])

        return sum
