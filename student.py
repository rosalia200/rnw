class Student:

    math= 0
    eng= 0
    swa= 0
    sci= 0
    soc= 20
    total = 0
    average=0

    def __init__(self,math,eng,swa,sci):

        self.math=math
        self.eng=eng
        self.swa=swa
        self.sci=sci

        self.total()
        self.average()
        self.mean()





    def total(self):
        self.total = self.math+ self.eng+self.swa+self.sci+self.soc
         #return self.total

    def average(self):
        self.average = self.total/5
         #return self.average
    def mean(self):
        if self.total>100:
            self.mean=self.total-self.soc
        else:
            self.mean=self.total-200
