class Solution:
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        points = sorted(points, key = lambda arrow: arrow[1]) #sort by end


        shootNum = 0


        for point in points:
            if shootNum == 0:
                curPoint = point
                shootNum += 1
                continue

            if point[0] <= curPoint[1]:
                continue
            else:
                curPoint = point
                shootNum += 1

        return shootNum
