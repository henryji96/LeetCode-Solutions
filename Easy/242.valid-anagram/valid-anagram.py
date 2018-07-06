from collections import Counter
class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return Counter(s) == Counter(t)

class Solution2:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sCnt = {}
        tCnt = {}

        for c in s:
            sCnt[c] = sCnt.get(c, 0)+ 1

        for c in t:
            tCnt[c] = tCnt.get(c, 0)+ 1

        return sCnt == tCnt
