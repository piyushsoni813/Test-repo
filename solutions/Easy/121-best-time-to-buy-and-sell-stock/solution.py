class Solution:
    def maxProfit(self, prices):
        current_min = prices[0]
        maxprofit = 0

        for i in range(1, len(prices)):
            today_profit = prices[i] - current_min

            if today_profit > maxprofit:
                maxprofit = today_profit

            if prices[i] < current_min:
                current_min = prices[i]

        return maxprofit