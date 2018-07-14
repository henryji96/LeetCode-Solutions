from collections import defaultdict
class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        map = defaultdict(str)

        for i in range(len(s)):
            a = s[i]
            b = t[i]

            if a in map:
                if map[a] == b:
                    continue
                else:
                    return False
            else:
                if b not in map.values():
                    map[a] = b
                else:
                    return False
        return True
