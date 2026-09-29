from abc import ABC, abstractmethod


class Employee(ABC):

    @abstractmethod
    def calculate_salary(self):
        pass


class FullTimeEmployee(Employee):

    def _init_(self, monthly_salary):
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary


class PartTimeEmployee(Employee):

    def _init_(self, hours, rate):
        self.hours = hours
        self.rate = rate

    def calculate_salary(self):
        return self.hours * self.rate


# Full-time employee
monthly_salary = float(input("Enter monthly salary of full-time employee: "))

full_time = FullTimeEmployee(monthly_salary)

print("Full-time salary:", full_time.calculate_salary())


# Part-time employee
hours = float(input("Enter working hours of part-time employee: "))
rate = float(input("Enter hourly rate: "))

part_time = PartTimeEmployee(hours, rate)

print("Part-time salary:", part_time.calculate_salary())