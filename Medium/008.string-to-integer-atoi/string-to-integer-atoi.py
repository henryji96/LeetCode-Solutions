import math
class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """

        str = str.strip()

        if str == "" or str =="+" or str == "-":
            return 0


        if str[0] == "+" and str[1].isdigit(): # +23223 - 23223
            isPos = True
            str = str[1:]
        elif str[0].isdigit():                 # 4242
            isPos = True
        elif str[0] == "-" and str[1].isdigit():  # -314 - 314
            isPos = False
            str = str[1:]
        else:
            return 0

        ans = ""
        upperBound = int(math.pow(2,31)) - 1
        lowerBound = int(math.pow(2,31)) #-

        for i in range(len(str)):
            if not str[i].isdigit():
                break
            if ans != "" and (isPos and int(ans) >= upperBound):
                return int(upperBound)
            elif ans != "" and (not isPos and int(ans) >= lowerBound):
                return -int(lowerBound)

            ans += str[i]


        if (isPos and int(ans) >= upperBound):
            return int(upperBound)
        elif (not isPos and int(ans) >= lowerBound):
            return -int(lowerBound)

        if isPos:
            return int(ans)
        else:
            return -int(ans)




        
