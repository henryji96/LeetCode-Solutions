class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == "":
            return []

        self.map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
            "0": " "
        }
        self.ans = []
        self.dfs(digits, 0, [])

        return self.ans

    def dfs(self, digits, i, tempArr):

        if len(digits) == len(tempArr):
            self.ans.append("".join(x for x in tempArr))
            return

        for char in self.map[digits[i]]:
            tempArr.append(char)
            self.dfs(digits, i + 1, tempArr)
            tempArr.pop()

        
