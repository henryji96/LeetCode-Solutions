class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        sl = s.split(" ")[::-1]

        ans = ""
        for word in sl:
            if word != "":
                ans = ans + word + " "
        return ans[:-1]


#One Line Solution
#return ' '.join(s.split()[::-1])
