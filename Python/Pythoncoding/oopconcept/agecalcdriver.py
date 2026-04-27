from idlelib.debugobj import make_objecttreeitem

from oopconcept.agecalc import Agecalculation
from oopconcept.myexception import AgeException

age =int(input('Age:'))

aobj =Agecalculation()
try:
    aobj.voting_age_check(age)
    aobj.pension_age_check(age)
    #if aobj.voting_age_check(age):
        #print('Eligible.Proceed to next step')
except AgeException as ae:
    print(ae)
else:
    print('Eligible.Proceed to next step')