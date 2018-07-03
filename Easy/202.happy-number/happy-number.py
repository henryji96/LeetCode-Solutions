class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def getSquaredSum(num):
            s = 0
            while num:
                s += (num%10)**2
                num = num // 10
            return s

        numSet = set()

        while n != 1:

            n = getSquaredSum(n)

            if n == 1:
                break

            if n in numSet:
                return False

            numSet.add(n)



        return True
