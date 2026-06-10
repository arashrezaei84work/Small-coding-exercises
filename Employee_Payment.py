from abc import ABC, abstractmethod


class Employ(ABC):
    def __init__(self, name: str, fname: str):
        self.name = name
        self.fname = fname

    def full_name(self):
        return f"{self.name} {self.fname}"

    @abstractmethod
    def calc_salary(self):
        pass


class FullTimeEmployee(Employ):
    def __init__(self, name, fname, monthly_salary: int):
        super().__init__(name, fname)
        self.monthly_salary = monthly_salary

    def calc_salary(self):
        return self.monthly_salary


class PartialTimeEmployee(Employ):
    def __init__(self, name, fname, hours_worked: int, hourly_salary: int):
        super().__init__(name, fname)
        self.hours_worked = hours_worked
        self.hourly_salary = hourly_salary

    def calc_salary(self):
        return self.hourly_salary * self.hours_worked


class FreeLancer(Employ):
    def __init__(self, name, fname, proj_number, proj_salary: int):
        super().__init__(name, fname)
        self.proj_number = proj_number
        self.proj_salary = proj_salary

    def calc_salary(self):
        return self.proj_number * self.proj_salary


ep1 = FullTimeEmployee("Arash", "Rezaei", 8000)
ep2 = PartialTimeEmployee("kourowsh", "Rezaei", 80, 25)
ep3 = FreeLancer("Reza", "Rezaei", 4, 1000)

print(ep3.calc_salary())
print(ep2.calc_salary())
print(ep1.calc_salary())
print(ep2.full_name())
