from datetime import datetime

class User :
    def __init__(self, name, email, address, account_type, passward, bank):
        self.account_no = None
        self.name = name 
        self.email = email
        self.address = address
        self.account_type = account_type
        self.passward = passward
        self.bank = bank
        self.balance = 0
        self.loan = 0
        self.taken_loan = 0
        self.transaction_history = []

    def diposit(self, amount): # provide a bank object
        self.balance += amount
        # add the amount to the bank's balance 
        self.bank.balance += amount

        self.transaction_history.append(f"Transaction Time : {datetime.now()} . Transaction Type : Diposit . Amount : {amount} . Balance : {self.balance} .")

    def withdraw(self, amount): # provide a bank object
        if(amount > self.balance):
            print("Withdrawal amount exceeded")
        elif(self.bank.bankrupt):
            print("The bank is bankrupt")
        else :
            self.balance -= amount
            self.bank.balance -= amount

            
            print(f"Congrats !!! Your Withdraw of {amount} Taka is Successfull .")
            
            self.transaction_history.append(f"Transaction Time : {datetime.now()} . Transaction Type : Withdraw . Amount : {amount} . Balance : {self.balance} .")
    
    def check_balance(self):
        print(f"Your Available Balance is = {self.balance}\n")
    
    def check_transaction_history(self):
        for i in self.transaction_history :
            print(i)
        print("")
    
    def take_loan(self, amount):
        if(self.taken_loan >= 2):
            print("Sorry!! Your loan taking limit is exited .")
        elif self.bank.loan_feature != True :
            print("Sorry !! The Loan Feature of the bank is off now .")
        elif self.bank.bankrupt == True :
            print("The bank is bankrupt")
        else :
            self.balance += amount
            self.bank.balance -= amount
            self.bank.given_loan += amount
            self.taken_loan += 1
            
            
            print(f"Congrats !!! You have successfully taken a loan of {amount} Taka .")
            self.transaction_history.append(f"Transaction Time : {datetime.now()} . Transaction Type : Loan Taken . Amount : {amount} . Balance : {self.balance} .")

    def transfer(self, account_no, amount):
        if(self.balance < amount):
            print("Sorry !! Insuficient Balance ")
            return
        
        ac = None
        for i in self.bank.users :
            if(i.account_no == account_no):
                ac = i
                break
        
        if ac == None :
            print("Account does not exist")
        else :
            self.balance -= amount
            ac.balance += amount

            
            print(f"Congrats !!! You have successfully transfered {amount} Taka .")
            
            self.transaction_history.append(f"Transaction Time : {datetime.now()} . Transaction Type : Transfered to {ac.name} . Amount : {amount} . Balance : {self.balance} .")

            ac.transaction_history.append(f"Transaction Time : {datetime.now()} . Transaction Type : Recived money from {self.name} . Amount : {amount} . Balance : {self.balance} .")
