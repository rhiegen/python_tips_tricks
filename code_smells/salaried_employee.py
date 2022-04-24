from dataclasses import dataclass
from code_smells.employee import Employee


@dataclass
class SalariedEmployee(Employee):
    monthly_salary: float = 5000

    def pay(self) -> None:
        print(f"Paying {self.name} the monthly salary of {self.monthly_salary}")
