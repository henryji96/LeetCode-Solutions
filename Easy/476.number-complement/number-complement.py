class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        ans = 0
        binary = bin(num)[2:]
        for index, bit in enumerate(binary[::-1]):
            if bit == '0':
                ans += 2**index
        return ans

if __name__ == '__main__':
    s = Solution()
    ans = s.findComplement(2)
    print(ans)
