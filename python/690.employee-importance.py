"""
# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        for i in employees:
            if id == i.id:
                l = list()
                l.append(id)
                break

        sum = 0

        while len(l) != 0:
            for i in employees:
                if i.id in l:
                    if len(i.subordinates) != 0:
                        for j in i.subordinates:
                            l.append(j)
                    l.remove(i.id)
                    sum += i.importance

        return sum

