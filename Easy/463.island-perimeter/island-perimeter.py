class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ans = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    ans += self.checkUpper(grid, i, j)
                    ans += self.checkLower(grid, i, j)
                    ans += self.checkLeft(grid, i, j)
                    ans += self.checkRight(grid, i, j)
        return ans

    def checkUpper(self, grid, i, j):
        if i == 0:
            return 1
        if grid[i-1][j] == 1:
            return 0
        else:
            return 1
    def checkLower(self, grid, i, j):
        if i == len(grid) - 1:
            return 1
        if grid[i+1][j] == 1:
            return 0
        else:
            return 1
    def checkLeft(self, grid, i, j):
        if j == 0:
            return 1
        if grid[i][j-1] == 1:
            return 0
        else:
            return 1
    def checkRight(self, grid, i, j):
        if j == len(grid[0]) - 1:
            return 1
        if grid[i][j+1] == 1:
            return 0
        else:
            return 1

class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        row = len(grid)
        col = len(grid[0])

        perimeter = 0
        overlap = 0

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    perimeter += 4

                    if(i > 0 and grid[i - 1][j] == 1):
                        overlap += 1
                    if(i < row - 1 and grid[i + 1][j] == 1):
                        overlap += 1
                    if(j > 0 and grid[i][j - 1] == 1):
                        overlap += 1
                    if(j < col - 1 and grid[i][j + 1] == 1):
                        overlap += 1
                        
        return perimeter - overlap
