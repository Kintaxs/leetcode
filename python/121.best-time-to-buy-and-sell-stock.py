class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        if(len(prices) == 0):
            return 0

        max_profit = 0
        min_value = prices[0]

        for i in prices:
            if(i > min_value):
                max_profit = max(max_profit, i - min_value)
            else:
                min_value = i

        return max_profit
