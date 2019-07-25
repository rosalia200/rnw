#create a payroll class
#gross_salary=basic_salary+benefits
#
class Payroll :
    basic_salary=0
    benefits =0
    payee=0
    nhif_deductions=0
    nssf_deductions=0
    gross_salary=0
    net_salary=0

    def __init__(self,bs,be,py,nh,nsd,gs,ns):
        Payroll.basic_salary=bs
        Payroll.benefits=be
        Payroll.payee=py
        nhif_deductions=nh
        nssf_deductions=nsd
        gross_salary=gs
        net_salary=ns

    def gross_salary(self):
        return self.basic_salary+self.benefits

    def payee(self):
        if self.gross_salary <12298:
            self.payee=10%self.gross_salary
        if self.gross_salary==23885-12298:
            self.payee==15%self.gross_salary
        if self.gross_salary==35472-23885











    def nhif_deduductions(self):
        return

