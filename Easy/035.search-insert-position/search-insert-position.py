class Solution:

    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i = 0
        for val in nums:
            if(target <= val):
                break
            i = i + 1
                
        return i