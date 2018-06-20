class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if r*c != len(nums)*len(nums[0]):
            return nums
        ans = []
        curRow = []
        cCut = 0

        for i in range(0, len(nums)):
            for j in range(0, len(nums[0])):

                cCut += 1
                curRow.append(nums[i][j])

                if cCut == c:
                    ans.append(curRow)
                    curRow = []
                    cCut = 0

        return ans
