from typing import override

from oopconcept.formulamethods import FM


class Rectangle(FM):
    def __init__(self,l,b):
        self.length=l
        self.breadth=b
    @override
    def calc_area(self):
        return self.length*self.breadth
    @override()
    def calc_peri(self):
        return 2*(self.length*self.breadth)