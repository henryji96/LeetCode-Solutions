class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        if len(nums) < 4:
            return []
        nums.sort()

        l = len(nums)
        ans = []

        for i in range(0, l - 3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, l - 2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue

                low = j + 1
                high = l - 1

                while low < high:
                    four = nums[i] + nums[j] + nums[low] + nums[high]
                    if four == target:
                        ans.append([nums[i], nums[j], nums[low], nums[high]])
                        while low < high and nums[low] == nums[low+1]:
                            low += 1
                        while low < high and nums[high] == nums[high - 1]:
                            high -= 1
                        high -= 1
                        low += 1
                    elif four > target:
                        high -= 1
                    elif four < target:
                        low += 1
        return ans
