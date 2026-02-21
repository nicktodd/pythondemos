# Single Responsibility Principle (SRP)
# A class should have only one reason to change

# BAD: This class has multiple responsibilities
class BadEmployee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def calculate_pay(self):
        """Calculate employee pay - FINANCIAL responsibility"""
        return self.salary * 1.1
    
    def save_to_database(self):
        """Save employee to database - PERSISTENCE responsibility"""
        print(f"Saving {self.name} to database...")
    
    def generate_report(self):
        """Generate employee report - REPORTING responsibility"""
        return f"Employee Report: {self.name}, Salary: {self.salary}"


# GOOD: Each class has a single responsibility
class Employee:
    """Responsible ONLY for employee data"""
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class PayrollCalculator:
    """Responsible ONLY for calculating pay"""
    def calculate_pay(self, employee):
        return employee.salary * 1.1


class EmployeeRepository:
    """Responsible ONLY for database operations"""
    def save(self, employee):
        print(f"Saving {employee.name} to database...")


class EmployeeReportGenerator:
    """Responsible ONLY for generating reports"""
    def generate_report(self, employee):
        return f"Employee Report: {employee.name}, Salary: {employee.salary}"


# Usage
if __name__ == "__main__":
    print("=== Bad Example ===")
    bad_emp = BadEmployee("Alice", 50000)
    print(bad_emp.calculate_pay())
    bad_emp.save_to_database()
    print(bad_emp.generate_report())
    
    print("\n=== Good Example ===")
    employee = Employee("Bob", 60000)
    
    payroll = PayrollCalculator()
    print(f"Pay: {payroll.calculate_pay(employee)}")
    
    repository = EmployeeRepository()
    repository.save(employee)
    
    report_gen = EmployeeReportGenerator()
    print(report_gen.generate_report(employee))
