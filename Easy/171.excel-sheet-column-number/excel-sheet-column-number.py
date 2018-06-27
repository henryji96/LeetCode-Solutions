class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """

        ans = 0
        base = 1
        for val in s[::-1]:
            ans += (ord(val) - ord('A') + 1) * base
            base *= 26

        return ans
