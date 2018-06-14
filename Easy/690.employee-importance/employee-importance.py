"""
# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution:
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """


        employeeDict = {}
        for e in employees:
            employeeDict[e.id] = e

        queue = employeeDict[id].subordinates
        totalVal = employeeDict[id].importance


        while len(queue) > 0:
            actualID = queue.pop(0)

            totalVal += employeeDict[actualID].importance
            queue = queue + employeeDict[actualID].subordinates

        return totalVal
