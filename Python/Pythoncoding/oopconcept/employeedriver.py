from oopconcept.employeedetails import Empdetails

#driver
eno = int(input('Emp no'))
name = input('Emp name')
bp = int(input('Basic pay'))

employee = Empdetails(empno=eno,ename=name,basicpay=bp)
print('Emp no:',employee.empno)
print('Emp name:',employee.ename)
print('Basic pay:',employee.basic_pay)
print('Salary:',employee.calc_netsal())
