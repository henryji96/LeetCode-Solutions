class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """

        ans = 0

        while(n > 4):
            ans += n // 5
            n = n // 5
        return ans
