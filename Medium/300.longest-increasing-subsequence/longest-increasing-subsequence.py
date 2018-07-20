from bisect import bisect_left
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        dp = []

        for num in nums:
            if dp == []:
                dp.append(num)
            if num > dp[-1]:
                dp.append(num)
            else:
                i = bisect_left(dp, num)
                dp[i] = num
        return len(dp)
