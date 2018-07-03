from bisect import bisect_left
class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i_l in range(len(numbers)):
            findTarget = target - numbers[i_l]
            findNums = numbers[i_l+1:]
            i_r = bisect_left(findNums, findTarget) + i_l + 1


            if i_r == len(numbers):
                continue
            elif numbers[i_r] == findTarget:
                return [i_l+1, i_r+1]

        
