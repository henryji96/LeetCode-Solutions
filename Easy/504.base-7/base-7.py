#weight approaching
import math
class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num < 0:
            ans = "-"
            num = abs(num)
        else:
            ans = ""

        maxExp = 0
        while math.pow(7, maxExp) <= num:
            maxExp += 1
        if maxExp != 0:
            maxExp -= 1


        weight = 0
        while maxExp >= 0:

            while weight*math.pow(7, maxExp) <= num:
                weight += 1
            if weight != 0:
                weight -= 1

            ans += str(weight)
            num -= weight * math.pow(7, maxExp)
            maxExp -= 1
            weight = 0
        return ans


class Solution2(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "0"

        ans = ""
        tempNum = abs(num)

        while tempNum != 0:

            rightBit = tempNum % 7
            tempNum = tempNum // 7

            ans = str(rightBit) + ans

        if num < 0:
            return "-"+ans
        else:
            return ans
