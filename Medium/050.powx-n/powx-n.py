import math
class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """

        return math.pow(x,n)


class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """

        if n < 0:
            x = 1.0 / x
            n = abs(n)

        if n == 0:
            return 1
        if n == 1:
            return x

        ret = self.myPow(x, n // 2)

        return ret*ret if n%2 == 0 else x*ret*ret
