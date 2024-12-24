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
        user.account_no = len(self.users) + 1 
        self.users.append(user)

    def add_admin(self, admin):
        self.admins.append(admin)