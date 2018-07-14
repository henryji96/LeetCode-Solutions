class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        self.ans = []

        self.dfs("", n, n)

        return self.ans 

    def dfs(self, tempStr, left, right):
        if left > right:
            return
        if left == 0 and right == 0:
            self.ans.append(tempStr)
            return

        if left:
            self.dfs(tempStr + '(', left - 1, right)
        if right:
            self.dfs(tempStr + ')', left, right - 1)
