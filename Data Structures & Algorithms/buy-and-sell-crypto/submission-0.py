class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0,0
        res = 0
        while r < len(prices):
            profit = prices[r] - prices[l]
            if prices[r] < prices[l]:
                l = r      
            r += 1
            res = max(res, profit)
        return res