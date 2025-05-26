"""
    Assignment 14: 
    Create a class Department and a class Employee. Use aggregation by having a Department 
    object store a reference to an Employee object that exists independently of it.
"""
class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def display_info(self):
        print(f"Employee ID: {self.emp_id}, Name: {self.name}")


class Department:
    def __init__(self, dept_name):
        self.dept_name = dept_name
        self.employees = []  # Aggregation: Department "has" Employees (but they exist independently)

    def add_employee(self, employee):
        self.employees.append(employee)

    def list_employees(self):
        print(f"Employees in {self.dept_name}:")
        for emp in self.employees:
            emp.display_info()


# Usage
if __name__ == "__main__":
    # Employees exist independently of departments
    emp1 = Employee("Ayesha", 1001)
    emp2 = Employee("Muhsin", 1002)

    # Create a department and add employees
    dept = Department("Engineering")
    dept.add_employee(emp1)
    dept.add_employee(emp2)

    # List employees in the department
    dept.list_employees()

    # Employees still exist even if the department is deleted
    emp1.display_info()