#Class 1
class Worker:
    def __init__(self, name,hours_worked, hourly_rate):
        self.name = name
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate
    
    def calculate_pay(self):
        """To be implemented by subclasses"""  
        raise NotImplementedError("Subclasses must implement this method")
    def __str__(self):
        return f"{self.name}: ${self.calculate_pay():.2f}"

class Employee(Worker):
    def calculate_pay(self):
        if self.hours_worked <= 40:
            return self.hours_worked * self.hourly_rate
        else:
            # Calculate overtime pay
            regular_pay = 40 * self.hourly_rate
            overtime_hours = self.hours_worked - 40
            overtime_pay = overtime_hours * self.hourly_rate * 1.5
            return regular_pay + overtime_pay

#Class 2
class Contractor(Worker):
    def calculate_pay(self):
        return self.hours_worked * self.hourly_rate
    
#Testing classes
workers=[
    Employee("Alice", 45, 20),
    Contractor("Bob", 30, 25),
    Employee("Charlie", 38, 22)
    ]

#Payroll calculation
print("Payroll Summary:\n-----------------")
for worker in workers:
    print(worker)