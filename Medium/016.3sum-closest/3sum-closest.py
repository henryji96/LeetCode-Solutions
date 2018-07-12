import sys
class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()

        minDiff = sys.maxsize

        for i in range(len(nums)-2):

            l = i + 1
            r = len(nums) - 1

            while l < r:

                diff = abs(target - nums[i] - nums[l] - nums[r])
                if diff < minDiff:
                    minDiff = diff
                    ans = nums[i] + nums[l] + nums[r]

                if target == nums[i] + nums[l] + nums[r]:
                    return nums[i] + nums[l] + nums[r]
                elif target > nums[i] + nums[l] + nums[r]:
                    l += 1
                else:
                    r -= 1


        return ans
