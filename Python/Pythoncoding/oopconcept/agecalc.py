from oopconcept.myexception import AgeException


class Agecalculation:
    def voting_age_check(self,age):
        if age<18:
            raise AgeException('Not eligible to vote')
        else:
            return True

    def pension_age_check(self,age):
        if age<60:
            raise AgeException('Not eligible for pension')
