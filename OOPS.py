# #1. Classes
class Person:
  name = "Nishi"
  occupation = "Student"
  year = 2

  def info(
      self
  ):  #self parameter is a referance to the current instance of the class and is used to access variables that belongs to the class.(voh object jiske liye method call ho rha hai)
    print(f"{self.name} is a {self.occupation}")


a = Person()
a.name = "Jigisha"
a.occupation = "Student"
a.info()


#2.
class Person:

  def __init__(self, n, o):
    print("Hello")
    self.name = n
    self.occupation = o

  def info(self):
    print(f"{self.name} is a {self.occupation}")


a = Person("Nishi", "Student")
b = Person("Jigisha", "Student")
a.info()
b.info()


#3.
class Person:

  def __init__(self, name, occ):
    self.name = name
    self.occupation = occ

  def __str__(
      self
  ):  #__str__ is a dunder method,used to define how a class object is converted to a string
    return f"{self.name} is a  {self.occupation}."


ans = Person("Nishi", "Student")
print(ans)

#4.


class Person(object):

  def __init__(self, name, occ):
    self.name = name
    self.occupation = occ

  def Display(self):
    print(self.name, self.occupation)


emp = Person("Nishi", "Student")
emp.Display()


class Emp(Person):

  def Print(self):
    print("Emp class called")


Emp_details = Emp("Jigisha", "student")

Emp_details.Display()

Emp_details.Print()

#5.referred gfg

# Python code to demonstrate how parent constructors
# are called.


# parent class
class Person(object):

  # __init__ is known as the constructor
  def __init__(self, name, idnumber):
    self.name = name
    self.idnumber = idnumber

  def display(self):
    print(self.name)
    print(self.idnumber)


# child class
class Employee(Person):

  def __init__(self, name, idnumber, salary, post):
    self.salary = salary
    self.post = post

    # invoking the __init__ of the parent class
    Person.__init__(self, name, idnumber)


# creation of an object variable or an instance
a = Employee('Rahul', 886012, 200000, "Intern")

# calling a function of the class Person using its instance
a.display()
