import math
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False

        log = math.log(n,2)
        print(log,round(log))
        return abs(log - int(log)) < 10e-10



class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        while n % 2 == 0:
            n /= 2
        return n == 1
