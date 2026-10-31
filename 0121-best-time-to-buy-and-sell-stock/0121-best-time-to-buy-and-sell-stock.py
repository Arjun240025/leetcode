class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy=prices[0]
        p=0
        for i in range(1,len(prices)):
            if prices[i]<buy:#lowest buy value
                buy=prices[i]
            if prices[i]-buy>p:#to find best sell price
                p=prices[i]-buy
        return p
        #     if prices[i]>prices[i-1]:
        #         p+=prices[i]-prices[i-1]
        # return p(for multiple transactions)
