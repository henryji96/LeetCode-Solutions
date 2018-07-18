class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        if len(pattern) != len(str.split(' ')):
            return False

        map = {}

        for p,s in zip(pattern, str.split(' ')):
            if p not in map:
                if s not in map.values():
                    map[p] = s
                else:
                    return False
            elif map[p] != s:
                return False
        return True
