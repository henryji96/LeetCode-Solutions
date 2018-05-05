class Solution:
    def longestCommonPrefix1(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if (len(strs)!=0):
            smallestLen = len(strs[0]) 
        else:
            return ""
        commonPre = 0
        
        for s in strs:
            if(smallestLen > len(s)):
                smallestLen = len(s)

        for i in range(0, smallestLen):
            c = []
            for s in strs:
                c.append(s[i])
           
            if(len(set(c)) == 1):
                commonPre += 1
            else:
                break
        return strs[0][0:commonPre]