class MyClass:
    def __init__(self,name):
        self.name = name
    def myfun(self):
        pass

    @staticmethod
    def display(self,m): # Here self is not representing to class. It is just a parameter
        print(m)


ob = MyClass("RAVAN")
ob.display(20,30)

# testing_venv\Scripts\activate.bat

