from collections import Counter
class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        rCnt = Counter(ransomNote)
        mCnt = Counter(magazine)

        for key, val in rCnt.items():
            if key in mCnt and val <= mCnt[key]:
                continue
            else:
                return False
        return True
        
