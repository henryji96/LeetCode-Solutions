class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        if g == [] or s == []:
            return 0

        s.sort()
        g.sort()
        ans = 0
        j = 0

        for greed in g:
            if (j == len(s)):
                return ans   #early stop

            while (j != len(s)) and (greed > s[j]):
                j += 1

            if (j != len(s)) :
                ans += 1
                j += 1
        return ans
