class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        low = 1
        high = x
        while low <= high:
            middle = low + (high - low) // 2
            if middle*middle > x:
                high = middle - 1
            else:
                low = middle + 1
        return high
if __name__ == '__main__':
    s = Solution()
    print(s.mySqrt(8))
