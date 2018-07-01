class Solution1:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        bitStr = ""

        for _ in range(32):
            if n!= 0:
                bitStr = str(n % 2) + bitStr
                n = n >> 1
            else:
                bitStr = "0" + bitStr

        return int(bitStr[::-1],2)


class Solution2:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):

        ans = 0

        for i in range(32):
            ans = (ans << 1) + (n & 1)
            n >>= 1

        return ans




if __name__ == '__main__':
    s = Solution()
    ans = s.reverseBits(43261596)
    print(ans)
