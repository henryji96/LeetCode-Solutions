import sys
class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(set(nums)) == 1:
            return nums[0]
        if len(set(nums)) == 2:
            return max(nums)


        m1, m2, m3 = -sys.maxsize, -sys.maxsize, -sys.maxsize

        for num in set(nums):
            if num > m1:
                m1, m2, m3 = num, m1, m2
            elif num > m2:
                m2, m3 = num, m2
            elif num > m3:
                m3 = num

        return m3

        
