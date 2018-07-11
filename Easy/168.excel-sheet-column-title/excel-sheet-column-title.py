class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        ans = ""
        while n:
            n -= 1
            ans = chr(ord('A') + n % 26) + ans
            n = n // 26
        return ans
