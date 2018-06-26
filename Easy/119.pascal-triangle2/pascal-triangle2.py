class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """

        ans = [1]

        for i in range(rowIndex):

            curRow = [0]*(len(ans)+1)

            curRow[0] = 1
            curRow[-1] = 1
            for j in range(1,len(curRow)-1):
                curRow[j] = ans[j-1] + ans[j]

            ans = curRow

        return ans
