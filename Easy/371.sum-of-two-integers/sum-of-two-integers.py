class Solution:
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """

        return sum([a, b])

import numpy as np
class Solution:
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        while b!= 0:
            c = (a & b) << 1
            a = np.int32(a ^ b)
            b = np.int32(c)
        return int(a)
        
