class Solution:
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """

        ans = []
        self.dfs(S, '', ans, 0)

        return ans

    def dfs(self, initS, changeS, ans, index):
        if index == len(initS):
            ans.append(changeS)
            return

        if initS[index].isalpha():
            self.dfs(initS, changeS + initS[index].upper(), ans, index + 1)
            self.dfs(initS, changeS + initS[index].lower(), ans, index + 1)
        else:
            self.dfs(initS, changeS + initS[index], ans, index + 1)

if __name__ == '__main__':
    s = Solution()
    ans = s.letterCasePermutation('a3eR4')
    print(ans)
