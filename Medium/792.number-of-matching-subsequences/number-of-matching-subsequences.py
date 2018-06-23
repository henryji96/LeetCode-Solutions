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
