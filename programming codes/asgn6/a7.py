
class student:
    h="hello"
    def __init__(self,name,branch,sid):
        self.name=name
        self.branch=branch
        self.sid=sid
        
    def std(self):
        print(f"{self.h},of student class")
class marks:
    gm=42
    def __init__(self,name,marks,sid):
        self.name=name
        self.marks=marks
        self.sid=sid

    def mm(self):
        print(f"{self.gm},is your marks")

a=student("abhilash","civil",22102069)
b=marks("abhilash",6.9,22102069)
print(a.name)
print(b.name,b.marks,b.sid)