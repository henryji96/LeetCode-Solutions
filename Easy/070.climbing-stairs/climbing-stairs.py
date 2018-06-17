class Solution:
    def climbStairs(self, n):
        """
            :type n: int
            :rtype: int
            """
        if n == 1:
            return 1
        elif n == 2:
            return 2
        
        dp = [0]*n
        dp[0] = 1
        dp[1] = 2
        
        for i in range(2, n):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[-1]



class Solution2:
    
    def climbStairs(self, n):
        """
            :type n: int
            :rtype: int
            """
        if n <= 1:
            return 1
        
        self.dp = [0] * n
        
        return self.numOfSolutions(n)
    
    def numOfSolutions(self, n):
        if n <= 1:
            return 1
        if self.dp[n - 1] > 0:           #记忆化递归，结果记下来，不要重复计算
            return self.dp[n - 1]
        
        self.dp[n - 1] = self.numOfSolutions(n - 1) + self.numOfSolutions(n - 2)
        
    return self.dp[n - 1]


