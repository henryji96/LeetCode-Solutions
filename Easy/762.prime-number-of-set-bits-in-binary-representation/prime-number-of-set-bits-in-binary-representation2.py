import math
class Solution:
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """

        cntIsPrime = 0
        for num in range(L,R+1):
            bit1Num = self.cntBits1(num)
            if self.isPrime(bit1Num):
                cntIsPrime += 1
        return cntIsPrime


    def cntBits1(self, num):
        cnt = 0
        while num > 0:
            cnt += num & 0b1
            num = num >> 1
        return cnt

    def isPrime(self, num):
        if num <= 1:
            return False
        elif num == 2:
            return True
        else:
            for i in range(2, int(math.sqrt(num))+1):
                if num % i == 0:
                    return False
            return True


if __name__ == '__main__':
    s = Solution()
    print(s.countPrimeSetBits(10,15))
