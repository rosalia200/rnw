class Student:
    name = ""
    age = 0
    gender = ""
    math= 0
    eng= 0
    swa= 0
    sci= 0
    soc= 0

    def __init__(self,n,a,g,math,eng,swa,sci,soc):
        Student.name = n
        Student.age =a
        Student.gender = g
        Student.math=math
        Student.eng=eng
        Student.swa=swa
        Student.sci=sci
        Student.soc=soc


    def total(self):
        return self.math+ self.eng+self.swa+self.sci+self.soc

    def average(self):
        return self.total/5