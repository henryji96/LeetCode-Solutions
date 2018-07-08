import bisect
class Solution:
    def maxProfitAssignment(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """
        difficulty_profit = []
        for i in range(len(profit)):
            difficulty_profit.append(difficulty[i], profit[i])
        difficulty_profit = sorted(difficulty_profit, key = lambda x: x[0])

        ans = 0
        for workerAbility in worker:
            i = 0
            maxProfit = 0
            while workerAbility <= difficulty_profit[i][0]:

                maxProfit = max(maxProfit, difficulty_profit[i][1])
                i += 1
            ans += maxProfit
        return ans
