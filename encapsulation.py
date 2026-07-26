import sys

class Student:
    def __init__(self,name):
        self.name = name
        self.__marks = 0  ### prefix __ variable name makes the variable as private variable

    def get_marks(self):  # getter method
        return self.__marks
    
    def set_mark(self,marks): # setter method
        if marks <=100:
            self.__marks = marks
        else:
            print("Invalid! Marks must be <=100")

# def main(args):
#     stu = Student("Rohan")

if __name__ == "__main__":
    stu = Student("Rohan")
    stu.set_mark(90)
    print(stu.get_marks())

