class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        ans = []

        for i in range(numRows):
            if ans == []:
                ans.append([1])
                continue

            lastRow = ans[-1]
            curRow = [0]*(len(lastRow)+1)
            curRow[0] = 1
            curRow[-1] = 1

            for j in range(1,len(curRow)-1):
                curRow[j] = lastRow[j-1] + lastRow[j]

            ans.append(curRow)

        return ans
