# parent class
class Person:
  #costructor made of two varriables
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  def printname(self):
    print(self.firstname, self.lastname)

#child class Student drived from Person
class Student(Person):

  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year
  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the 1st class of", self.graduationyear)

x = Student("supriya", "Madansure",2023)
x.printname() #this function is drived from its base class
x.welcome()
