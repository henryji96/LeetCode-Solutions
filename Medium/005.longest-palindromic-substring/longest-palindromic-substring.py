class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        if s == "" or len(s) == 1:
            return s

        res = ""

        for i in range(len(s)-1):
            p1 = self.helper(s, i, i)    # cabac  中心扩展法
            p2 = self.helper(s, i, i+1)  # cbbc

            if len(p1) > len(res):
                res = p1
            if len(p2) > len(res):
                res = p2
        return res


    def helper(self, s, left, right):
        while (left >= 0 and right <= len(s) - 1) and s[left] == s[right]:
            left -= 1
            right += 1

        if right == left:
            return s[right]
        else:
            return s[left + 1:right]
