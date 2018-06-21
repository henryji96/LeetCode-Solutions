class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        if len(g) == 0 or len(s) == 0:
            return 0

        s.sort()
        g.sort()
        ans = 0

        for greed in g:
            while (len(s) != 0) and (greed > s[0]):
                del s[0]
            if (len(s) != 0):
                ans += 1
                del s[0]
        return ans
