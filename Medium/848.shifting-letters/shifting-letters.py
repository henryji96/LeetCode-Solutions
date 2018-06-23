# Get the ASCII number of a character
#number = ord(char)

# Get the character given by an ASCII number
#char = chr(number)

'''
TLE O(N^2)
class Solution(object):
    def shiftingLetters(self, S, shifts):
        """
        :type S: str
        :type shifts: List[int]
        :rtype: str
        """
        for i in range(len(shifts)):
            for j in range(i + 1):
                S = S[:j] + self.shift(S[j], shifts[i]) + S[j+1:]
        return S

    def shift(self, c, num):
        return chr((ord(c) - ord('a') + num) % 26 + ord("a"))
'''

class Solution(object):
    def shiftingLetters(self, S, shifts):
        """
        :type S: str
        :type shifts: List[int]
        :rtype: str
        """
        shiftsLen = len(shifts)
        shiftNum = 0
        for i in range(shiftsLen):
            index = shiftsLen - i - 1
            shiftNum += shifts[index]

            shiftChr = chr( (ord(S[index]) - ord('a') + shiftNum) % 26 + ord('a') )
            S = S[:index] + shiftChr + S[index+1:]
        return S
