class Solution:
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        if num == 1:
            return True

        while(num >= 2):
            if num % 2 == 0:
                num /= 2
            elif num % 3 == 0:
                num /= 3
            elif num % 5 == 0:
                num /= 5
            else:
                return False
        return True

if __name__ == '__main__':
    s = Solution()
    print(s.isUgly(6))
    print(s.isUgly(14))
