class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, word):
                    return True
        return False

    def dfs(self, board, i, j, word):
        if len(word) == 0:
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return False
        if word[0] != board[i][j]:
            return False

        temp = board[i][j]   # first character is found, check the remaining part
        board[i][j] = '#'    # avoid visit agian

        ans = self.dfs(board, i+1, j, word[1:]) or self.dfs(board, i-1, j, word[1:]) \
            or self.dfs(board, i, j-1, word[1:]) or self.dfs(board, i, j+1, word[1:])

        board[i][j] = temp

        return ans
