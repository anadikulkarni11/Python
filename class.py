class student:
    
    def __init__(self):
        self.rollno=1
        self.name="ab"
    def marks(self,m1,m2,m3,p=0):
        self.M1=m1;
        self.M2=m2;
        self.M3=m3;
        self.P=(self.M1+self.M2+self.M3)/3
        if self.P>=75:
          print("Grade A")
        elif self.P>=60:
          print("Grade B")
        else:
          print("Grade C")
        
             
    def printv(self):
        print("Roll number=",self.rollno)
        print("Name=",self.name)
s1=student()
s1.marks(78,89,90)
s1.printv()

