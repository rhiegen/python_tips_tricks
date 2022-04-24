from code_smells.company import Company
from code_smells.hourly_employee import HourlyEmployee
from code_smells.role import Role
from code_smells.salaried_employee import SalariedEmployee


def main() -> None:
    company = Company()
    company.add_employees(SalariedEmployee(name="John", role=Role.MANAGER))
    company.add_employees(HourlyEmployee("Bob", Role.PRESIDENT))
    company.add_employees(HourlyEmployee("Jill", Role.INTERN))
    print(company.find_employees(Role.PRESIDENT))
    print(company.find_employees(Role.MANAGER))
    print(company.find_employees(Role.INTERN))
    company.employees[0].pay()
    company.employees[0].take_a_holiday()


if __name__ == '__main__':
    main()
