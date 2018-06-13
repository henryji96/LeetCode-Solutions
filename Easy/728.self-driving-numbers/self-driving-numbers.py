class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        ansList = []
        for num in range(left, right + 1):
            if self.isSelfDriving(num):
                ansList.append(num)

        return ansList


    def isSelfDriving(self, num):
        numOrg = num
        isSelfDrivingNum = True

        while num != 0:
            lowBit = num % 10

            if(lowBit == 0):
                isSelfDrivingNum = False
                break

            if(numOrg % lowBit != 0):
                isSelfDrivingNum = False
                break

            num = num // 10

        return isSelfDrivingNum
if __name__ == '__main__':
    s = Solution()
    ans = s.selfDividingNumbers(1, 22)
    print(ans)
