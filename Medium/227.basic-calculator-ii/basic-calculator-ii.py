class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """

        nums = []
        op = '+'

        temp = 0
        i = 0
        while i < len(s):

            if s[i] == " ":
                continue

            if s[i].isdigit():
                temp = 10 * temp + int(s[i])
            if s[i] in "=-*/":
                if op in "+-":
                    prev = 0
                else:
                    prev = nums.pop()
                nums.append(self.calcTwo(prev, temp, op))
                num = 0

                op = s[i]
            i += 1

        return sum(nums)




    def calcTwo(self, a, b, op):
        if op == "+":
            return a + b
        elif op == "-":
            return a - b
        elif op == "*":
            return a * b
        elif op == "/":
            return a / b
