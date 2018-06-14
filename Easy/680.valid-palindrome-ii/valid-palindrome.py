class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """


        for i in range(len(s)//2 + 1):
            left = i
            right = len(s) - 1 - i

            if s[left] != s[right]:
                if self.isPalindrome(s, left + 1, right) or self.isPalindrome(s, left, right - 1):
                    return True
                else:
                    return False




        return True



    def isPalindrome(self, s, left, right):

        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True




if __name__ == '__main__':
    s = Solution()
    print(s.validPalindrome("abca"))
