class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """

        sums = sum(nums[:k])
        res = sums

        for i in range(k,len(nums)):
            sums += nums[i] - nums[i-k]
            if sums > res:
                res = sums


        return res / float(k)
        
