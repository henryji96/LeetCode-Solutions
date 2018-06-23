class Solution(object):
    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        def isMatch(S, words):

            nextStartIndex = 0
            for c in words:
                nextStartIndex = S.find(c, nextStartIndex) + 1
                if nextStartIndex == 0:
                    return False
            return True


        return sum(isMatch(S, word) for word in words)

##############################################################
import bisect
class Solution2(object):
    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """

        sCharPos = {}
        for i in range(len(S)):
            if S[i] not in sCharPos.keys():
                sCharPos[S[i]] = [i]
            else:
                sCharPos[S[i]].append(i)

        return sum(self.isMatch(sCharPos, word) for word in words)


    def isMatch(self, sCharPos, word):

        nextStart = 0
        for c in word:
            if c in sCharPos:
                cIndexList = sCharPos[c]
                i = bisect.bisect_right(cIndexList, nextStart)

                if i < len(cIndexList):
                    nextStart = cIndexList[i]
                else:
                    return False
            else:
                return False
        return True
