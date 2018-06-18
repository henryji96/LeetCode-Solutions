class Solution1(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_sort = sorted(nums)

        return max(nums_sort[-1] * nums_sort[-2] * nums_sort[-3],
                   nums_sort[-1] * nums_sort[0] * nums_sort[1])

import sys
class Solution2(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max1, max2, max3, min1, min2 = -sys.maxsize,-sys.maxsize,-sys.maxsize,sys.maxsize,sys.maxsize

        for num in nums:
            if(max1 < num):
                max3, max2, max1 = max2, max1, num
            elif(max2 < num):
                max3, max2 = max2, num
            elif(max3 < num):
                max3 = num

            if(min1 > num):
                min2, min1 = min1, num
            elif(min2 > num):
                min2 = num
        return max(max1*max2*max3, max1*min1*min2)
