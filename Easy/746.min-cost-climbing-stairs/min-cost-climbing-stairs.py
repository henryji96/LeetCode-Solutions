class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """

        dp0, dp1, dp2 = 0, 0, 0

        for i in range(2, len(cost)+1):
            dp2 = min(dp1 + cost[i-1], dp0 + cost[i-2])
            dp0, dp1 = dp1,dp2

        return dp2

if __name__ == '__main__':
    s = Solution()
    print(s.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
