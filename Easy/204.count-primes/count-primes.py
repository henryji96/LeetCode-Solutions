class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n is None or n <= 2:
            return 0
        isPrime = [True] * n
        isPrime[0] = False
        isPrime[1] = False

        i = 2
        while i * i < n:
            if isPrime[i]:
                j = i
                while i * j < n:
                    isPrime[i * j] = False
                    j += 1
            i += 1

        return sum(isPrime)
