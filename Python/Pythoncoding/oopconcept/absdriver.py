from oopconcept.rectangle import Rectangle
from oopconcept.square import Square

sqobj = Square(10)
print(f'Area:{sqobj.calc_area()} \tPerimeter:{sqobj.calc_peri()}')

recobj=Rectangle(10,5)
print(f'Area:{recobj.calc_area()} \tPerimeter:{recobj.calc_peri()}')