class Employee:
    _company_bonus = 300

    def __init__(self, name, salary):
        self.__name = str(name)
        self.__salary = float(salary)
        self.__bonus = 0

    @property
    def name(self):
        return self.__name

    @property
    def salary(self):
        return self.__salary

    def set_bonus(self, bonus=_company_bonus):
        self.__bonus = bonus

    @property
    def bonus(self):
        return self.__bonus

    def to_pay(self):
        return self.__salary + self.__bonus


class SalesPerson(Employee):
    def __init__(self, name, salary, percent_completed=100):
        """
        :param percent_completed: if the sales person completed the plan more than 100%, his bonus is doubled,
        if more than 200% - tripled.
        """
        super().__init__(name, salary)
        self.__percent_completed = percent_completed

    def set_bonus(self, bonus=Employee._company_bonus):
        if 100 < self.__percent_completed <= 200:
            bonus *= 2
        elif self.__percent_completed > 200:
            bonus *= 3
        super().set_bonus(bonus)


class Manager(Employee):
    def __init__(self, name, salary, client_amount):
        super().__init__(name, salary)
        self.__client_amount = client_amount

    def set_bonus(self, bonus=Employee._company_bonus):
        if 100 < self.__client_amount <= 150:
            bonus += 500
        elif self.__client_amount > 150:
            bonus += 1000
        super().set_bonus(bonus)


class Company:
    def __init__(self, *args):
        self.__employees = list(args)

    @property
    def employees(self):
        """
        :return: a list of Employee objects
        """
        return self.__employees

    def give_everybody_bonus(self):
        """
        Metod sets bonus for every employee
        """
        for employee in self.__employees:
            employee.set_bonus()

    def total_to_pay(self):
        """
        :return: Total amount of money (salaries + bonuses)
        """
        total = 0
        for employee in self.__employees:
            total += employee.to_pay()
        return total

    def name_max_salary(self):
        """
        :return: Name property of the instance of Employee class with highest Salary property
        """
        max_salary_employee = None
        max_salary = 0
        for employee in self.__employees:
            if employee.salary > max_salary:
                max_salary = employee.salary
                max_salary_employee = employee
        return max_salary_employee.name


if __name__ == '__main__':
    # Demonstrate the Employee class
    print('\nCreate instance of the class Employee: empl = Employee("John", 1000)')
    empl = Employee('John', 1000)
    print(f'Name property: {empl.name}')
    print(f'Salary property: {empl.salary:.2f}')
    print('Set default Bonus empl.set_bonus()')
    empl.set_bonus()
    print(f'Bonus value: {empl.bonus:.2f} (default value)')
    print(f'Total pay (method to_pay): {empl.to_pay():.2f}')

    # Create SalesPerson instances
    print('\nCreate instances of the class SalesPerson which inherits from the Employee class:')
    print('salesman100 = SalesPerson("Dwight", salary=2000)')
    print('salesman101 = SalesPerson("Jim", salary=2000, percent_completed=101)')
    print('salesman240 = SalesPerson("Pam", salary=2000, percent_completed=240)')
    salesman100 = SalesPerson('Dwight', salary=2000)
    salesman101 = SalesPerson("Jim", salary=2000, percent_completed=101)
    salesman240 = SalesPerson("Pam", salary=2000, percent_completed=240)

    # Set bonuses for salesmen
    print('Set Bonus for salesman100: salesman100.set_bonus(300)')
    salesman100.set_bonus(300)
    print(f'Bonus value: {salesman100.bonus:.2f}')
    print('Set Bonus for salesman101: salesman101.set_bonus(300)')
    salesman101.set_bonus(300)
    print(f'Bonus value: {salesman101.bonus:.2f}')
    print('Set Bonus for salesman240: salesman240.set_bonus(300)')
    salesman240.set_bonus(300)
    print(f'Bonus value: {salesman240.bonus:.2f}')
    # Total pay for salesmen (salary+bonus)
    print(f'Total pay for each salesman (method to_pay): {salesman100.to_pay()}, {salesman101.to_pay()}, '
          f'{salesman240.to_pay():.2f}')

    # Create Manager instances
    print('\nCreate instance of the class Manager: manager50 = Manager("Bob", salary=3000, client_amount=50)')
    manager50 = Manager('Bob', salary=3000, client_amount=50)
    print('Create instance of the class Manager: manager120 = Manager("Michael", salary=3000, client_amount=120)')
    manager120 = Manager('Michael', salary=3000, client_amount=120)
    print('Create instance of the class Manager: manager800 = Manager("David", salary=4000, client_amount=800)')
    manager800 = Manager('David', salary=4000, client_amount=800)

    # Set bonuses for managers
    print('Set bonus for manager50: manager50.set_bonus()')
    manager50.set_bonus()
    print(f'Bonus value: {manager50.bonus:.2f}')
    print('Set bonus for manager120: manager120.set_bonus()')
    manager120.set_bonus()
    print(f'Bonus value: {manager120.bonus:.2f}')
    print('Set bonus for manager170: manager170.set_bonus()')
    manager800.set_bonus()
    print(f'Bonus value: {manager800.bonus:.2f}')
    print(f'Total pay for each manager (method to_pay): {manager50.to_pay():.2f}, {manager120.to_pay():.2f}, '
          f'{manager800.to_pay():.2f}')

    print('\n=================Advanced Level=====================')

    print('\nCreate instance of the class Company: company = Company(empl, salesman100, salesman101, salesman240, '
          'manager50, manager120, manager800)')
    company = Company(empl, salesman100, salesman101, salesman240, manager50, manager120, manager800)
    print('Give everybody bonus: company.give_everybody_bonus()')
    company.give_everybody_bonus()
    print('Print all names, salaries and bonuses: ')
    for employee in company.employees:
        print(f"{employee.name}'s salary: {employee.salary:.2f}. Bonus: {employee.bonus:.2f}")

    print(f'\nTotal to pay: {company.total_to_pay():.2f}')
    print(f'The highest paid employee: {company.name_max_salary()}')
