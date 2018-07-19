class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        first = self.findFirst(nums, target)
        last = self.findLast(nums, target)

        return [first,last]

    def findFirst(self, nums, target):
        low = 0
        high = len(nums) - 1

        ans = -1
        while low <= high:
            mid = low + (high - low) // 2

            if target <= nums[mid]:
                high = mid - 1
            else:
                low = mid + 1

            if nums[mid] == target:
                ans = mid
        return ans

    def findLast(self, nums, target):
        low = 0
        high = len(nums) - 1

        ans = -1
        while low <= high:
            mid = low + (high - low) // 2

            if target >= nums[mid]:
                low = mid + 1
            else:
                high = mid - 1

            if nums[mid] == target:
                ans = mid
        return ans
