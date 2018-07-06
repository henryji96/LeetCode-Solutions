import math
class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False

        log3 = math.log(n,3)
        if abs(round(log3,0) - log3) < 0.0000000000001:
            return True
        return False

class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """

        if n <= 0:
            return False

        while n % 3 == 0:
            n /= 3
        return n == 1
