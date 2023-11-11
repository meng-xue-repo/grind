class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxVal = [None] * len(prices)
        maxVal[-1] = prices[-1]

        for i in reversed(range(len(prices) - 1)):
            maxVal[i] =  prices[i] if prices[i] > maxVal[i + 1] else maxVal[i + 1]

        res = 0
        for i in range(len(prices) - 1):
            diff = maxVal[i + 1] - prices[i]
            if diff > res:
                res = diff

        return res
