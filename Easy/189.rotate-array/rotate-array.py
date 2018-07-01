class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        

        for _ in range(k):
            right = nums.pop()
            nums.insert(0,right)
