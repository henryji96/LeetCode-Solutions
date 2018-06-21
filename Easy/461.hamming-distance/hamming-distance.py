class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        ans = 0

        while x != 0 or y != 0:
            xBit = x % 2
            yBit = y % 2

            ans += (xBit ^ yBit)

            x = x // 2
            y = y // 2

        return ans

            
