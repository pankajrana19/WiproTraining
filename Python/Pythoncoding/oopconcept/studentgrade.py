from oopconcept.student import Student


class Studentgrade(Student):
    def __init__(self,ccode,cname,ccity,rno,sname,m1,m2,m3):
        super().__init__(ccode,cname,ccity,rno,sname,m1,m2,m3)
        self.result=''
        self.grade=None

    def calc_res(self):
        if self.mark1>40 and self.mark2>40 and self.mark3>40:
            self.result='Pass'
        else:
            self.result='Fail'

    def calc_grd(self):
        self.calc_res()
        if self.result=='Pass':
            avg =super().calc_avg()
            if avg >= 80.0:
                self.grade='A'
            elif avg >=60.0:
                self.grade='B'
            elif avg >=40.0:
                self.grade='C'
            else:
                self.grade='NA'