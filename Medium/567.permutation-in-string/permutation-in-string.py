from collections import Counter
class Solution:
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        s1Dict = dict(Counter(s1))
        s1Len = len(s1)


        s2SlideDict = {}

        # sliding window
        for i in range(len(s2)):
            if s2[i] not in s2SlideDict:
                s2SlideDict[s2[i]] = 1
            else:
                s2SlideDict[s2[i]] += 1


            if i >= s1Len:
                if s2SlideDict[s2[i - s1Len]] == 1:
                    del s2SlideDict[s2[i - s1Len]]
                else:
                    s2SlideDict[s2[i - s1Len]] -= 1

            if s2SlideDict == s1Dict:
                return True

        return False
