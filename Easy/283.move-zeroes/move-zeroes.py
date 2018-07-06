class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        nonZero = []
        zero = []
        for num in nums:
            if num != 0:
                nonZero.append(num)
            else:
                zero.append(0)

        nums[0:len(nonZero)-1] = nonZero
        nums[len(nonZero):] = zero


class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        totalZero = nums.count(0)
        for i in range(totalZero):
            nums.remove(0)
            nums.append(0)

class Solution(object):
    def moveZeroes(self, v):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        v[:] = [i for i in v if i != 0 ]+[0 for i in range(v.count(0))]
        
