class Solution:
    def isPalindrome1(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if(x < 0):
            return False
        xStr = str(x)
        reverse_xStr = xStr[::-1]
        if(x == int(reverse_xStr)):
            return True
        else:
            return False
        
    def isPalindrome2(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        half = 0
        while x > half:
            half = half * 10 + x % 10
            x /= 10
        return x == half or half / 10 == x

