from mypack.basicshapes import periofsquare,areaofsquare
from mypack.circle import areaofcircle, perimeterofcircle

radius =int(input('Enter radius'))

areaofcircle(rad=radius)
print(areaofcircle(rad=radius))
print(perimeterofcircle(rad=radius))

s=int(input('Enter side'))
print(areaofsquare(side=s))
print(periofsquare(side=s))