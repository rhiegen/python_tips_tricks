from abc import ABC, abstractmethod
from dataclasses import dataclass
from code_smells.custom_error import VacationDaysShortageError
from code_smells.role import Role

FIXED_VACATION_DAYS_PAYOUT = 5


@dataclass
class Employee(ABC):
    name: str
    role: Role
    vacation_days: int = 25

    def take_a_holiday(self) -> None:
        """let the employee take a single holiday """
        if self.vacation_days < 1:
            raise VacationDaysShortageError(
                requested_days=1,
                remaining_days=self.vacation_days,
                message="You don't have any vacation days left. Back to work!"
            )
        self.vacation_days -= 1
        print(f'Took a holiday. Vacation days left: {self.vacation_days}')

    def pay_out_a_holiday(self) -> None:
        """ Let the employee get paid for a holiday """
        if self.vacation_days < FIXED_VACATION_DAYS_PAYOUT:
            raise VacationDaysShortageError(
                requested_days=FIXED_VACATION_DAYS_PAYOUT,
                remaining_days=self.vacation_days,
                message="Not enough vacation days for a holiday"
            )

        self.take_a_holiday -= FIXED_VACATION_DAYS_PAYOUT
        print(f"Paying out a holiday. Holiday days left: {self.vacation_days}")

    @abstractmethod
    def pay(self) -> None:
        pass
