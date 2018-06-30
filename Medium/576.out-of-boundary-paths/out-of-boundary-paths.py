class Solution:
    def findPaths(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """

        dp = [[[0 for i in range(n)] for i in range(m)] for i in range(N+1)]
        adjs = [[1,0], [-1,0], [0,1], [0,-1]]

        for nMoveTimes in range(1,N+1):
            for row in range(m):
                for col in range(n):
                    for adj in adjs:
                        adjRow = row + adj[0]
                        adjCol = col + adj[1]

                        if adjRow < 0 or adjCol < 0 or adjRow == m or adjCol == n:
                            dp[nMoveTimes][row][col] += 1
                        else:
                            dp[nMoveTimes][row][col] += dp[nMoveTimes-1][adjRow][adjCol]
                            dp[nMoveTimes][row][col] %= 1000000007
        return dp[N][i][j]



                    
