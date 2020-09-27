class Employee:
  'Common base class for all employees'
  empCount = 0

  def __init__(self, name, salary):
    self.name = name
    self.salary = salary
    Employee.empCount += 1
 
  def displayCount(self):
    print('Total Employee {0}'.format(Employee.empCount))

  def displayEmployee(self):
    print('Name : {0} , Salary: {1}'.format(self.name, self.salary))

print("Employee.__doc__: {0}", Employee.__doc__)
print("Employee.__name__: {0}", Employee.__name__)
print("Employee.__module__:{0}", Employee.__module__)
print("Employee.__bases__:{0}", Employee.__bases__)
print("Employee.__dict__:{0}", Employee.__dict__)
print('\n\n')

"This would create first object of Employee class"
emp1 = Employee("Zara", 2000)

"This would create second object of Employee class"
emp2 = Employee("Manni", 5000)

emp1.displayEmployee()
emp2.displayEmployee()

print('Total Employee {0}'.format(Employee.empCount))

emp1.age = 7  # Add an 'age' attribute.
emp1.age = 8  # Modify 'age' attribute.
del emp1.age  # Delete 'age' attribute.

emp1.displayEmployee()
emp2.displayEmployee()

hasattr(emp1, 'age')    # Returns true if 'age' attribute exists
setattr(emp1, 'age', 8) # Set attribute 'age' at 8
getattr(emp1, 'age')    # Returns value of 'age' attribute
delattr(emp1, 'age')    # Delete attribute 'age'

emp1.displayEmployee()
emp2.displayEmployee()
