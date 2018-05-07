class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
        slow = 0
        for i, num in enumerate(nums):
            if(nums[i] == val):
                continue
            nums[slow] = nums[i]
            slow = slow + 1
        return slow