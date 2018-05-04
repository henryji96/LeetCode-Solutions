class Solution:
    def isPalindrome(self, x):
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