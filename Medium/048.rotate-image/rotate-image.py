class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])

        for i in range(row):
            for j in range(i+1):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp

        for i in range(row):
            for j in range(col//2):
                temp = matrix[i][j]
                matrix[i][j] = matrix[i][col - 1 - j]
                matrix[i][col - 1 - j] = temp



                
