class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(len(nums) == 0):
            return -1
            
        leftSum = 0
        rightSum = sum(nums) - nums[0]
        if rightSum == 0:
            return 0

        for i in range(1, len(nums)):

            leftSum = leftSum + nums[i - 1]
            rightSum = rightSum - nums[i]

            if(leftSum == rightSum):
                return i

        return -1

if __name__ == '__main__':
    s = Solution()
    ans = s.pivotIndex([1, 7, 3, 6, 5, 6])
    print(ans)
