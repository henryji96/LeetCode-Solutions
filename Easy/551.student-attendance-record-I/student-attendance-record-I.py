class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) < 2:
            return True
        if len(s) == 2 and s[0] == "A" and s[1] == "A":
            return False


        aNum = 0
        if s[0] == "A":
            aNum += 1
        if s[1] == "A":
            aNum += 1


        for i in range(2, len(s)):

            if s[i-2] == "L" and s[i-1] == "L" and s[i] == "L":
                return False

            if s[i] == "A":
                aNum += 1
                if aNum >=2:
                    return False
        return True



class Solution2(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) < 2:
            return True

        aNum = 0
        lNum = 0
        for c in s:
            if c == "A":
                aNum += 1

            if c == "L":
                lNum += 1
            else:
                lNum = 0

            if aNum >= 2 or lNum >= 3:
                return False
        return True
