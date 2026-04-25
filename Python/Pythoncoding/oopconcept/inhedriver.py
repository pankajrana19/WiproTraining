from oopconcept.college import College
from oopconcept.student import Student
from oopconcept.studentgrade import Studentgrade
from oopconcept.teacher import Teacher

cc=int(input('C code'))
cn =input('C name')
ci =input('City')

rno=int(input('Roll no'))
sn=input('Stu name')
m1=int(input('M1'))
m2=int(input('M2'))
m3=int(input('M3'))
eid=int(input('Eid'))
tn=input('Teach name')
de=input('Dept name')
bp=float(input('Basicpay'))


'''project = College(ccode=cc,cname=cn,ccity=ci)

project.welcome_message()
project.display_college_details()'''

'''project = Student(ccode=cc,cname=cn,ccity=ci,rno=rno,sname=sn,m1=m1,m2=m2,m3=m3)'''

project = Studentgrade(ccode=cc,cname=cn,ccity=ci,rno=rno,sname=sn,m1=m1,m2=m2,m3=m3)

project.welcome_message()
project.display_college_details()
print(f'Roll no:{project.rollno} \t name:{project.stname} \nTotal: {project.calc_total()} \nAverage: {project.calc_avg()}')
project.calc_grd()
print(f'Result:{project.result} \nGrade:{project.grade}')

teach = Teacher(ccode=cc,cname=cn,ccity=ci,eid=eid,tn=tn,de=de,bp=bp)
print(f'Eid:{teach.empid} \tName:{teach.tname} \tDept:{teach.dept}')
print(f'Salary:{teach.calc_sal()}')