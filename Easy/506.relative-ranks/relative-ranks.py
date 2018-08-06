class Solution:
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """

        if len(nums) == 0:
            return []
        elif len(nums) == 1:
            return ['Gold Medal']
        elif len(nums) == 2:
            if nums[0] > nums[1]:
                return ['Gold Medal', 'Silver Medal']
            else:
                return ['Silver Medal', 'Gold Medal']

        nSort = sorted(nums, reverse = True)

        for i, val in enumerate(nums):
            if val == nSort[0]:
                nums[i] = 'Gold Medal'
            elif val == nSort[1]:
                nums[i] = 'Silver Medal'
            elif val == nSort[2]:
                nums[i] = 'Bronze Medal'
            else:
                nums[i] = str(nSort.index(val) + 1)
        return nums


class Solution2:
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if len(nums) == 0:
            return []
        elif len(nums) == 1:
            return ['Gold Medal']
        elif len(nums) == 2:
            if nums[0] > nums[1]:
                return ['Gold Medal', 'Silver Medal']
            else:
                return ['Silver Medal', 'Gold Medal']


        numsDesc = sorted(nums, reverse = True)
        map = {}

        l = len(nums)
        map[numsDesc[0]] = 'Gold Medal'
        map[numsDesc[1]] = 'Silver Medal'
        map[numsDesc[2]] = 'Bronze Medal'

        for i in range(3, len(numsDesc)):
            map[numsDesc[i]] = str(i + 1)

        return [map[v] for v in nums]
