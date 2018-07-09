class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return -1
        if len(s) == 1:
            return 0

        for i in range(len(s)):
            if i == len(s) - 1:
                other = s[:-1]
            else:
                other = s[:i]+s[i+1:]

            if s[i] not in other:
                return i

        return -1



class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """

        for i in range(len(s)):
            c = s[i]
            if s.count(c)==1:
                return i

        return -1
        
    def firstUniqChar2(self, s):

        from collections import Counter
        sc = Counter(s)
        for i in range(len(s)):
            c = s[i]
            if sc.get(c,0)==1:
                return i

        return -1


from collections import defaultdict
import sys
class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        cPos = defaultdict(list)
        for i in range(len(s)):
            cPos[s[i]].append(i)

        hasUnique = False
        ans = sys.maxsize
        for key, val in cPos.items():
            if len(val) == 1:
                hasUnique = True
                ans = min(ans, val[0])

        if hasUnique:
            return ans
        else:
            return -1
