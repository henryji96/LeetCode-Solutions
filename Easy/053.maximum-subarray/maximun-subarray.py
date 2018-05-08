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