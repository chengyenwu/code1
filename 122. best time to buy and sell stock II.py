# 122. Best time to buy and sell stock II
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # dynamic programming
        profit=0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += (prices[i] - prices[i-1])
        return profit