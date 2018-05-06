class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rmNum = []
        for i, val in enumerate(nums):
            if(i > 0 and nums[i] == nums[i-1]):
                rmNum.append(nums[i-1])
        for val in rmNum:
            nums.remove(val)
                
        return len(nums)