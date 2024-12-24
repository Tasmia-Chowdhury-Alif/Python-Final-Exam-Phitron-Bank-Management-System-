from admin import Admin
from bank import Bank
from user import User

bd_bank = Bank("Bangladesh Bank")

hijbu = User("Hijbu","hijbu@gmail.com","abcd","current",bd_bank)
bd_bank.add_user(hijbu)
hijbu.diposit(1000)

jishan = User("Jishan","jishan@gmail.com","dfad","current",bd_bank)
bd_bank.add_user(jishan)
jishan.diposit(5000)

ad = Admin("admin","123",bd_bank)
bd_bank.add_admin(ad)

while True:
    print()
    print("1. Create an User account")
    print("2. Create an Admin account")
    print("3. Log in as Admin")
    print("4. Exit\n")
    
    c0 = int(input("Enter Your choise : "))

    if c0 == 1 :
        name = input("Enter Your Name : ")
        email = input("Enter Your Email : ")
        address = input("Enter Your Address : ")
        account_type = input("Enter Your account type : ")

        userr = User(name,email,address,account_type,bd_bank)
        bd_bank.add_user(userr)
        print()

        while True :
            print()
            print("1. Diposi Amount")
            print("2. Withdraw Amount")
            print("3. Check Available balance")
            print("4. Check transaction history")
            print("5. Take a loan from the Bank")
            print("6. Transfer amount to another user account")
            print("7. Exit\n")
            
            c1 = int(input("Enter Your choise : "))

            if c1 == 1 :
                amount = int(input("Enter Diposit Amount : "))
                userr.diposit(amount)
                print(f"Congrats !!! Your Diposit of {amount} Taka is Successfull .")
            elif c1 == 2 :
                amount = int(input("Enter Withdraw Amount : "))
                userr.withdraw(amount)
            elif c1 == 3 :
                userr.check_balance()
            elif c1 == 4 :
                userr.check_transaction_history()
            elif c1 == 5 :
                amount = int(input("Enter Loan Amount : "))
                userr.take_loan(amount)
            elif c1 == 6 :
                ac = int(input("Enter Reciver Account Number : "))
                amount = int(input("Enter Transfer Amount : "))
                userr.transfer(ac,amount)
            else:
                break
    elif c0 == 2 or c0 == 3 :
        name = input("Enter your Name : ")
        passward = input("Enter your Passward : ")
        add = None
        if c0 == 2 :
            add = Admin(name,passward,bd_bank)
            bd_bank.add_admin(add)
            print("\nSuccessfully Created an Admin Account .")
        else:
            for i in bd_bank.admins :
                if(i.name == name and i.get_passward == passward):
                    add = i
                    break
            if(add == None) :
                print("Invalid Name or Passward .")
                continue
            print("\nWellcome As Admin .")
        
        while True :
            print()
            print("1. Delete any user account ")
            print("2. See all user accounts list")
            print("3. Check the total available balance of the bank")
            print("4. Check the total loan amount of the bank")
            print("5. Turn On the loan feature")
            print("6. Turn Off the loan feature")
            print("7. Exit\n")

            c1 = int(input("Enter Your choise : "))

            if c1 == 1 :
                ac_no = int(input("Enter the Account no to Delete : "))
                ad.delete_user(ac_no)
                print(f"\nSuccessfully Deleted the Account no {ac_no}")
            elif c1 == 2 :
                ad.see_all_users()
            elif c1 == 3 :
                ad.check_balance()
            elif c1 == 4 :
                ad.check_loan()
            elif c1 == 5 :
                ad.loan_feature_on()
                print("\nSuccessfully Turned ON the loan Feature .")
            elif c1 == 6 :
                ad.loan_feature_off()
                print("\nSuccessfully Turned OFF the loan Feature .")
            else:
                break
    else :
        break

