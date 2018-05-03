class Solution:
    def reverse(self, x):
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