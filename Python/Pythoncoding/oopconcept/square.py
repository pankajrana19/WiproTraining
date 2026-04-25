from typing import override

from oopconcept.formulamethods import FM


class Square(FM):
    def __init__(self,s):
        self.side=s
    @override
    def calc_area(self):
        return self.side*self.side
    @override()
    def calc_peri(self):
        return 4*self.side