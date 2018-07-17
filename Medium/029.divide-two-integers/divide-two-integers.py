class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """

        if divisor == 0:
            return 2**31 - 1
        if dividend == -2**31:
            if divisor == -1:
                return 2**31 - 1
            elif divisor == 1:
                return -2**31


        sign = 1

        if dividend < 0:
            dividend = -dividend
            sign = -sign
        if divisor < 0:
            divisor = -divisor
            sign = - sign

        ans = 0
        while dividend >= divisor:
            shift = 0

            while dividend >= (divisor << shift):
                shift += 1

            ans += 1 << (shift - 1)
            dividend -= divisor << (shift - 1)

        if sign < 0:
            return -ans
        return ans
