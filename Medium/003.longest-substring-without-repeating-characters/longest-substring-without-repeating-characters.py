class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return 0
        if len(s) == 1:
            return 1

        subString = ""
        ans = ""
        lastIndex = {}

        for i in range(len(s)):

            if s[i] in subString:
                subString = s[lastIndex[s[i]]+1:i+1]
            else:
                subString += s[i]

            if len(subString) > len(ans):
                ans = subString
            lastIndex[s[i]] = i


        return len(ans)
