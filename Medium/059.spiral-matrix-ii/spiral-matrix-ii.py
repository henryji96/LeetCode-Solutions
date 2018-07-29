class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """

        res = [[0]*n for i in range(n)]
        val = 1

        rowBegin = 0
        rowEnd = len(res) - 1
        colBegin = 0
        colEnd = len(res) - 1

        while rowBegin <= rowEnd and colBegin <= colEnd:
            for i in range(colBegin, colEnd + 1):
                res[rowBegin][i] = val
                val += 1
            rowBegin += 1

            for i in range(rowBegin, rowEnd + 1):
                res[i][colEnd] = val
                val += 1
            colEnd -= 1

            if rowBegin <= rowEnd:
                for i in range(colEnd, colBegin - 1, -1):
                    res[rowEnd][i] = val
                    val += 1
                rowEnd -= 1

            if colBegin <= colEnd:
                for i in range(rowEnd, rowBegin - 1, -1):
                    res[i][colBegin] = val
                    val += 1
                colBegin += 1
        return res
