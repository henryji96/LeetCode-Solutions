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
    
    def removeDuplicates2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)
        slow = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[slow]:
                slow += 1
                nums[slow] = nums[i]
        return slow + 1