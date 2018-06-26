class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == "":
            return True


        allAlpha = ""
        for c in s.lower():
            if c.isalpha() or c.isnumeric():
                allAlpha += c

        return allAlpha == allAlpha[::-1]
