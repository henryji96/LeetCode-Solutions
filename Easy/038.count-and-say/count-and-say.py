class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        ans = "1"
        for i in range(1,n):
            ans = self.sayNum(ans)
        return ans
#     recursion   
#     def countAndSay(self, n):
#         """
#         :type n: int
#         :rtype: str
#         """
#         if n == 1:
#             return "1"
#         return self.sayNum(self.countAndSay1(n - 1))
            
    
    def sayNum(self, nums):
        
        
        numsStr = str(nums)
        cnt = 1
        prevNum = numsStr[0]
        ans = ""
        
        if(len(numsStr) == 1):
            return "1" + numsStr
        
        for i in range(1, len(numsStr)):
            if(numsStr[i] == numsStr[i-1]):
                cnt = cnt + 1
            else:
                ans = ans + str(cnt) + numsStr[i-1]
                cnt = 1
            if(i == len(numsStr)-1):
                ans = ans + str(cnt) + numsStr[i] 
        return ans
    
           