class Bank :
    def __init__(self, name):
        self.name = name
        self.balance = 9000000
        self.given_loan = 0
        self.users = []
        self.admins = []
        self.bankrupt = False
        self.loan_feature = True
 
    def add_user(self, user):
        user.account_no = len(self.users) + 100 
        self.users.append(user)

    def login_user(self, name, passward):
        for i in self.users :
            if(i.name == name and i.passward == passward):
                return i 

    def add_admin(self, admin):
        self.admins.append(admin)

    def login_admin(self, name, passward):
        for i in self.admins :
            if(i.name == name and i.get_passward == passward):
                return i 
