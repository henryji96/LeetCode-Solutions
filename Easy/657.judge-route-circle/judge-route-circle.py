class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        record = [0]*4 # R L U D

        for motion in moves:
            if motion != "\"":
                if motion == "R":
                    record[0] += 1
                elif motion == "L":
                    record[1] += 1
                elif motion == "U":
                    record[2] += 1
                elif motion == "D":
                    record[3] += 1

        if record[0] == record[1] and record[2] == record[3]:
            return True
        else:
            return False
