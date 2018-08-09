class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        return nums[-k]


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums or len(nums) == 0:
            return 0
        left = 0
        right = len(nums) - 1

        while 1:
            pos = self.partition(nums, left, right)
            if pos + 1 == k:
                return nums[pos]
            elif pos + 1 > k:
                right = pos - 1
            else:
                left = pos + 1



    def partition(self, nums, left, right):     # the left is the nth largest num
        pivot = nums[left]

        l = left + 1
        r = right

        while l <= r:
            if (nums[l] < pivot and nums[r] > pivot):
                self.swap(nums, l, r)
                l += 1
                r -= 1
            if nums[l] >= pivot:
                l += 1
            if nums[r] =< pivot:
                r -= 1
        self.swap(nums, left, r)
        return r

    def swap(self, nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
