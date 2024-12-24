class Admin:
    def __init__(self, name, passward, assigned_bank):
        self.name = name 
        self.__passward = passward
        self.bank = assigned_bank

    @property
    def get_passward(self):
        return self.__passward
    
    def delete_user(self, account_no):
        ac = None
        for i in self.bank.users :
            if i.account_no == account_no :
                ac = i
                break 
        
        if ac == None :
            print("Invalid account no .")
        else :
            self.bank.users.remove(i)

    def see_all_users(self):
        for i in self.bank.users :
            print(f"Name : {i.name} . Account No : {i.account_no} . Email : {i.email} . Address : {i.address} . Account type : {i.account_type} .")
        print()
    
    def check_balance(self):
        print(f"The total Available balance of {self.bank.name} is {self.bank.balance}")

    def check_loan(self):
        print(f"The total given loan of the Bank {self.bank.name} is {self.bank.given_loan}")
    
    def loan_feature_on(self):
        self.bank.loan_feature = True
    
    def loan_feature_off(self):
        self.bank.loan_feature = False

    def make_bankrupt(self):
        self.bank.bankrupt = True
