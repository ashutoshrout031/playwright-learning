class Student:
    def __init__(self,sid,sname,sgrade):
        self.sid = sid
        self.sname = sname 
        self.sgrade = sgrade

    def displaystu(self):
        print(f"EID: {self.sid}, emp_name: {self.sname}, salary: {self.sgrade}")