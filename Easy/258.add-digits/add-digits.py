class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num >= 10:
            num = self.getSum(num)

        return num


    def getSum(self, num):
        ans = 0
        while num:
            ans += (num % 10)
            num = num // 10
        return ans
