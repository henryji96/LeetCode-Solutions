class Solution:
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """

        score = []
        i = 0
        for op in ops:

            if op != "+" and op != "D" and op != "C":
                score.append(int(op))
                i += 1
            elif op == "+":
                score.append(score[i - 1] + score[i - 2])
                i += 1
            elif op == "D":
                score.append(score[i - 1] * 2)
                i += 1
            elif op == "C":
                del score[i - 1]
                i -= 1


        return sum(score)



if __name__ == '__main__':
    s = Solution()
    print(s.calPoints(["5","-2","4","C","D","9","+","+"]))
