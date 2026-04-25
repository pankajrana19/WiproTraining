from abc import ABC


class FM(ABC):
    '''@abstractmethod'''
    def calc_area(self):
        print('Area from FM')
    '''@abstractmethod'''
    def calc_peri(self):
        print('Peri from FM')