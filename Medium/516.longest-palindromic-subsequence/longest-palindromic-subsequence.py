class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        sLen = len(s)

        dp = [[0 for j in range(sLen)] for i in range(sLen)]

        for Len in range(1, sLen + 1):
            for i in range(0,sLen + 1 - Len):
                j = i + Len - 1

                if(i == j):
                    dp[i][j] = 1
                    continue

                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][sLen-1]
