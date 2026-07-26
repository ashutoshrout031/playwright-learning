import sys

sys.path.append("D:/Programs/Python Playwright/pack1")
from emp import Employee 

sys.path.append("D:/Programs/Python Playwright/pack2")
from stu import Student 


myemp = Employee(101,"John",4000)

myemp.displayemp()

mystd = Student(111,"Kiran","A")

mystd.displaystu()
