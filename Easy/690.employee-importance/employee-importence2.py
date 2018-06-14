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
        employeeDict = {e.id: e for e in employees}

        def dfs(id):

            actualEmp = employeeDict[id]

            subImportance = sum([dfs(subID) for subID in actualEmp.subordinates])

            return subImportance + actualEmp.importance

        return dfs(id)
