import re

'''txt = input('Enter a text')
bpat = input('Enter beginning pattern')
epat = input('Enter ending pattern')
bpat = '^'+bpat
epat = epat+'$'

if re.search(pattern=bpat ,string=txt):
    print('Beginning pat available')
else:
    print('Beginning pat not available')

if re.search(pattern=epat ,string=txt):
    print('Ending pat available')
else:
    print('Ending pat not available')'''

#digit
'''mbno = input('Enter a text')
pat = r"\d"

if re.fullmatch(pattern=pat,string=mbno):
    print('Only digits')
else:
    print('Other chars available')'''

#username
un = input('Enter UN')
pat = r"[a-z]{8}"

if re.match(pattern=pat,string=un):
    print('Valid')
else:
    print('Invalid')


#email
em = input('Enter email')
pat = r"[a-zA-Z0-9_]+@[a-z]+\.[a-z]+$"

if re.match(pattern=pat,string=em):
    print('Valid')
else:
    print('Invalid')


#pwd
pwd = input('Enter pwd')
pat = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[@_-]).{8,}$"

if re.match(pattern=pat,string=pwd):
    print('valid')
else:
    print('invalid')

txt = input('Text')
pat = r"\s+"

print(re.sub(pattern=pat,string=txt,repl=' '))
print(re.split(pattern=pat,string=txt))


