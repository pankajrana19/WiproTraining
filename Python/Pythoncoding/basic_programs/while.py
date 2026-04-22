#natural no print
"""num =int(input("Enter num"))
val=1

while val<=num:
    print(val)
    val +=1"""

#armstrong number
num=input("Enter a number")
ct=len(num)
sum=0
ni=int(num)
comp=ni

while ni>0:
    rem=ni%10
    sum=sum+rem**ct
    ni=ni//10

if comp==sum:
    print("Armstrong num")
else:
    print("Not Armstrong")