class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """


        tempSum = len(nums)*(len(nums) + 1) // 2
        

        return tempSum - sum(nums)
