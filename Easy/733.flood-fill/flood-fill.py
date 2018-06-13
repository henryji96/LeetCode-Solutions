class Solution:
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """

        if(image[sr][sc] == newColor):
            return image

        rowNum = len(image)
        colNum = len(image[0])

        self.dfs(image, sr, sc, rowNum, colNum, image[sr][sc], newColor)

        return image

    def dfs(self, image, row, col, rowNum, colNum, orgColor, newColor):

        if(row < 0 or col < 0 or row == rowNum or col == colNum):
            return

        if(image[row][col] != orgColor):
            return

        image[row][col] = newColor
        self.dfs(image, row + 1, col, rowNum, colNum, orgColor, newColor)
        self.dfs(image, row - 1, col, rowNum, colNum, orgColor, newColor)
        self.dfs(image, row, col + 1, rowNum, colNum, orgColor, newColor)
        self.dfs(image, row, col - 1, rowNum, colNum, orgColor, newColor)
        
if __name__ == '__main__':
    s = Solution()
    print(s.floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2))
