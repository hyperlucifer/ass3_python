# Define a class Employee having members id, name, department, salary. Create
# a subclass called manager with member bonus. Define methods accept and display in 
# both the classes. Create n objects of the manager class and 
# display the details of the manager having the maximum total salary (salary+bonus).

class Employee:
    def __init__(self) -> None:
        self.id=None
        self.name=None
        self.department=None
        self.salary=None

    def accept_employee_details(self):
        self.id=int(input("enter the employee id \n"))
        self.name=input("enter the employee name \n")
        self.department=input("enter the employee department \n")
        self.salary=int(input("enter the employee salary \n"))
    
    def display_employee_details(self):
    
        print(f"the id of the employee is {self.id}")
        print(f"the name of the employee is {self.name}")
        print(f"the department of the employee is {self.department}")
        print(f"the salary of the employee is {self.salary}")

class manager(Employee):
    def __init__(self) -> None:
        super().__init__()
        self.bonus=0
    
    def accept_employee_bonus(self):
       self.bonus=int(input("enter the employee bonus \n"))

    def display_employee_bonus(self):
        print(f"the bonus is {self.bonus}")

    def total_salary(self):
        return self.salary + self.bonus

n=int(input("enter the number of employes \n"))
man=[]
for i in range(n):
    obj=manager()
    obj.accept_employee_details()
    obj.accept_employee_bonus()
    man.append(obj)

max_sal=max(man,key=lambda m:m.total_salary())
print("\nManager with the highest total salary:")
max_sal.display_employee_details()
max_sal.display_employee_bonus()
print(f"Total Salary (Salary + Bonus): {max_sal.total_salary()}")


