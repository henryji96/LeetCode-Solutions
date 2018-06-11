class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """

        pDict = {}
        for value in p:
            if value not in pDict.keys():
                pDict[value] = 1
            else:
                pDict[value] = pDict[value] + 1
        pNum = sum(pDict.values())

        ans = []
        sDict = {}
        for index,value in enumerate(s):
            if value not in sDict.keys():
                sDict[value] = 1
            else:
                sDict[value] = sDict[value] + 1

            if sum(sDict.values()) == pNum + 1:
                if (index - pNum) >= 0 and sDict[s[index - pNum]] == 1:
                    del sDict[s[index - pNum]]
                elif (index - pNum) >= 0 and sDict[s[index - pNum]] > 1:
                    sDict[s[index - pNum]]  = sDict[s[index - pNum]] - 1
            if pDict == sDict:
                ans.append(index - pNum + 1)

        return ans






if __name__ == '__main__':
    s = Solution()
    ans = s.findAnagrams('cbaebabacd', 'abc')
    print(ans)
