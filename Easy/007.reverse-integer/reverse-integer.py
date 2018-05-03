class Solution:
    def reverse1(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = 0
        result = []
        reverseInt = 0
        
        if(x < 0):
            flag = 1

        temp = abs(x)

        while(temp != 0):
            result.append(temp % 10)
            temp = int(temp / 10)

        for i in range(len(result)):
            reverseInt += result[i]*(10**(len(result)-i-1))


        if ((flag == 0) & (reverseInt <= 2**31-1)):
            return reverseInt
        elif ((flag == 1) & (-reverseInt >= -2**31-1)):
            return -reverseInt
        else:
            return 0
        
        
    def reverse2(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = x < 0 and -1 or 1
        x = abs(x)
        ans = 0
        while x:
            ans = ans * 10 + x % 10
            x /= 10
        return sign * ans if ans <= 0x7fffffff else 0