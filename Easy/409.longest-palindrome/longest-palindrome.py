from collections import Counter
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """

        sDict = dict(Counter(s))
        ans = 0
        existOrder = 0

        for num in sDict.values():
            ans += num // 2
            if num % 2 != 0:
                existOrder = 1


        return ans * 2 + existOrder

if __name__ == '__main__':
    print(s.longestPalindrome("abccccdd"))
