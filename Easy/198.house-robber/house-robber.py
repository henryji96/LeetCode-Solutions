class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
            
        dp0 = nums[0]
        dp1 = max(nums[0], nums[1])
        dp2 = 0
        for i in range(2, len(nums)):
            dp2 = max(dp0 + nums[i], dp1)
            dp0, dp1 = dp1, dp2
        return dp2

if __name__ == '__main__':
    s = Solution()
    print(s.rob([1,2,3,1]))
