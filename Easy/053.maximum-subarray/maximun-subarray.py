# nums   [-1, 2, -2, 4, -8, 5, -9, 6]
# curSum [-1, 3,  1, 5,  0, 5,  0, 6]

class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curSum = 0
        maxSum = nums[0]

        for num in nums:
            if(curSum <= 0):
                curSum = 0

            curSum = curSum + num

            maxSum = max(curSum, maxSum)
        return maxSum
