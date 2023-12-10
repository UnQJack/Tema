class Employee:
    """Common base class for all employees"""
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.tasks = {}
        Employee.empCount += 1

    def display_emp_count(self):
        "Displays the number of employees"
        print(f"Total number of employee(s) is {Employee.empCount}")

    def display_employee(self):
        print("Name: ",self.name,", Salary: ",self.salary)

    def __del__(self):
        Employee.empCount -=1


    def update_salary(self, new_salary):
        self.salary = new_salary

##    def add_task(self, task_name):
##        self.tasks[task_name] = "New"   # needs tasks defined before (in __init__)
##
##    def update_tasks(self, task_name, status):
##        self.tasks[task_name] = status
        
    def modify_task(self, task_name, status="New"):
        self.tasks[task_name]=status

    def display_task(self, status):
        print(f"Taskuri cu statusul {status}")
        for name in self.tasks.keys():
            if self.tasks[name] == status:
                print(name)

class Manager(Employee):
    """Class representing a manager, inheriting from Employee"""
    mgrCount = 0

    def __init__(self,name,salary,department):
        super().__init__(name,salary)
        self.department = "F08"
        Manager.mgrCount += 1

    def display_employee(self):
        print("Salary: ",self.salary)

    def display_emp_count(self):
        "Displays the number of employees"
        print(f"Total number of employee(s) is {Manager.mgrCount}")    

m1=Manager("M1",5000,"Marketing")
m2=Manager("M2",6000,"Sales")
m3=Manager("M3",7000,"Development")
m4=Manager("M4",8000,"Finance")
m5=Manager("M5",9000,"HR")

m1.display_employee()
m2.display_employee()
m3.display_employee()
m4.display_employee()
m5.display_employee()

e1=Employee("E1",4000)
e2=Employee("E2",4500)

e1.display_employee()
e2.display_employee()

print(e1.empCount)
print(m1.mgrCount)


import pytest

from ex1 import Employee, Manager

emp_count=0

def test_employee_creation():
    e=Employee("E1",7500)
    assert e.name == "E1"
    assert e.salary == 7500
    Employee.emp_count += 1
    
mgr_count=0

def test_manager_creation():
    m=Manager("M1",10000,"D1")
    assert m.name == "M1"
    assert m.salary == 10000
    assert m.department == "D1"
    Manager.mgr_count += 1

def test_display_employee():
    e=Employee("E1",7500)
    assert e.display_employee() == "Name: E1, Salary: 7500"

def test_display_manager():
    m=Manager("M1",10000,"D1")
    assert m.display_employee() == "Salary: 10000"


