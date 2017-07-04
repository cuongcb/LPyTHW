# Ex42 from LPyTHW - Is-A, Has-A, Objects and Classes

## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    def __init__(self):
        print "Animal is created...\n"

class Dog(Animal):
    def __init__(self, name):
        print "Dog is created...\n"
        print "%s is created...\n" % name
        self.name = name

class Cat(Animal):
    def __init__(self, name):
        print "Cat is created...\n"
        print "%s is created...\n" % name
        self.name = name

class Person(object):
    def __init__(self, name):
        print "Person is created...\n"
        print "%s is created...\n" % name
        self.name = name
        self.pet = None

class Employee(Person):
    def __init__(self, name, salary):
        super(Employee, self).__init__(name)
        print "Employee is created...\n"
        self.salary = salary

class Fish(object):
    def __init__(self):
        print "Fish is created...\n"

class Salmon(Fish):
    def __init__(self):
        print "Salmon is created...\n"

class Halibut(Fish):
    def __init__(self):
        print "Halibut is created...\n"

rover = Dog("Rover")

satan = Cat("Satan")

mary = Person("Mary")
mary.pet = satan

frank = Employee("Frank", 120000)
frank.pet = rover

flipper = Fish()

crouse = Salmon()

harry = Halibut()
