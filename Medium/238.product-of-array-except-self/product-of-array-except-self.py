class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """


        p = 1
        n = len(nums)
        ans = [1] * len(nums)
        for i in range(n):
            ans[i] = p
            p = p * nums[i]


        p = 1
        for i in range(n-1, -1, -1):
            ans[i] *= p
            p *= nums[i]

        return ans
