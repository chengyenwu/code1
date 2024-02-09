# 121. Best time to buy and sell stock
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        buy = prices[0]
        sell = 0
        for price in prices[1:]:
            buy = min(buy, price)
            sell = max(sell, price-buy)
        return sell
    
        # if len(prices) < 2:
        #     return 0
        # buy = prices[0]
        # sell = 0
        # for i in range(len(prices)):
        #     if prices[i] < buy:
        #         buy = prices[i]
        #     if prices[i] >= buy:
        #         sell = max(sell, prices[i]-buy)
        # return sell