class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices == None or len(prices) < 2:
            return 0

        maxProfit = 0
        minPrice = prices[0]
        for price in prices:
            minPrice = min(minPrice, price)
            maxProfit = max(maxProfit, price - minPrice)
        return maxProfit
if __name__ == '__main__':
    s = Solution()
    maxProfit = s.maxProfit([7,1,5,3,6,4])
    print(maxProfit)
print(max)
