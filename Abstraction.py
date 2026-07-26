# If you create an abstract method then the class must be abstract
# ABC - Abstract Base Class
# Data abstraction  means showing only the essential features and hiding the complex internal details
# Giving the access on functionality but hiding implementation


from abc import ABC,abstractmethod

# Abstract class (Extenteded the ABC) 
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def stop(self):
        pass

# Concrete class( implemented abstract methods from abstract class)
class Car(Vehicle):
    def start(self):
        print("Car engine Started...")
    
    def stop(self):
        print("Car Engine stopped...")

# v= Vehicle cannot create object for the abstract class

c =  Car()
c.start()
c.stop()


# We can't hide the implementation here so Python is not fully supported to data abstraction
# In Java if you use AbstractClass ref = new ChildClass() then you can't see the implementation
