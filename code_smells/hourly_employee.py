from dataclasses import dataclass

from code_smells.employee import Employee


@dataclass
class HourlyEmployee(Employee):
    hourly_rate_dollars: float = 50
    hours_worked = 10

    def pay(self) -> None:
        print(f"Paying employee{self.name} a hourly rate of \
                          ${self.hourly_rate_dollars} for {self.hours_worked} hours worked")