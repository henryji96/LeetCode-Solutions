class Solution:
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """

        ans = ''
        for i in range(0, len(s), 2*k):
            ans += (s[i:i+k][::-1] + s[i+k:i+2*k])

        return ans
        
