class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
            return False


        row, col = 0, len(matrix[0]) - 1
        while row < len(matrix)-1:
            if matrix[row][col] < target:
                row += 1
            else:
                break

        return self.binarySearch(matrix[row], target)

    def binarySearch(self, arr, target):

        low, high = 0, len(arr) - 1

        while low <= high:

            mid = low + (high - low) // 2

            if arr[mid] == target:
                return True
            elif arr[mid] > target:
                high -= 1
            else:
                low += 1
        return False
