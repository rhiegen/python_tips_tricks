from typing import List
from code_smells.employee import Employee
from code_smells.role import Role


class Company:
    def __init__(self) -> None:
        self.employees: List[Employee] = []

    def add_employees(self, employee: Employee) -> None:
        self.employees.append(employee)

    def find_employees(self, role: Role) -> List[Employee]:
        # list comprehension
        return [employee for employee in self.employees if employee.role is role]
