from typing import List

class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        def fun(id):
            for employee in employees:
                if employee.id==id:
                    break
            if employee.subordinates==[]:
                return employee.importance
            res=0
            for i in employee.subordinates:
                res+=fun(i)
            return res+employee.importance
        return fun(id)