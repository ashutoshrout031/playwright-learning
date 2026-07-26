class Employee:
    def __init__(self,eid,ename,sal):
        self.eid = eid
        self.ename = ename 
        self.sal = sal

    def displayemp(self):
        print(f"EID: {self.eid}, emp_name: {self.ename}, salary: {self.sal}")