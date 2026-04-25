from oopconcept.college import College


class Student(College):
    def __init__(self,ccode,cname,ccity,rno,sname,m1,m2,m3):
        super().__init__(ccode,cname,ccity)
        self.rollno=rno
        self.stname=sname
        self.mark1=m1
        self.mark2=m2
        self.mark3=m3

    def calc_total(self):
        return self.mark1+self.mark2+self.mark3

    def calc_avg(self):
        return self.calc_total()/3
