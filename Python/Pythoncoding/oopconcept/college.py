class College:
    def __init__(self,ccode,cname,ccity):
        self.ccode=ccode
        self.cname=cname
        self.ccity=ccity
    def welcome_message(self):
        print('Hello there!!!')
    def display_college_details(self):
        print(f'College code: {self.ccode} \n College name: {self.cname} \n College city: {self.ccity}')

