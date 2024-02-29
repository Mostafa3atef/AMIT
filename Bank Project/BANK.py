class Bank_Account:
    def __init__(self):
        self.users_usenames=['mostafa','ahmed']
        self.users_passwords=['12345','123123']
        self.users_balances=[6000,1000]

    def check(self,username,password,new_acc):
        if new_acc==True:
            if username in self.users_usenames:
                print("Username already exists.")
                return
            else:
                self.users_usenames.append(username)
                self.users_passwords.append(password)
                print("User registered successfully.")
                return 
        trials=0
        while username in self.users_usenames and trials<2:
            if password in self.users_passwords:
                print(f'Welcome {username}')
                return "ENTER"
            else:
                print("Wrong password, try again")
                trials+=1
                password=str(input("Enter Password: "))
                
        if trials==2:
            return
        else:
            print("Username is not registered")

    def login(self,user_name_input,user_password_input):
        new_acc=False
        return self.check(user_name_input,user_password_input,new_acc)

    def registeration(self):
        new_user=str(input("Enter a unique username: "))
        new_password=str(input("Enter new password: "))
        new_acc=True
        self.check(new_user,new_password,new_acc)

    def check_balance(self,user_for_balance):
        print(f'Balance= {self.users_balances[self.users_usenames.index(user_for_balance)]} LE')

    def deposit(self,user_for_deposit):
        amount=int(input("Enter amount to be Deposited: "))
        if amount>0:
            self.users_balances[self.users_usenames.index(user_for_deposit)]= self.users_balances[self.users_usenames.index(user_for_deposit)]+amount
            print(f'Processing...\n{amount} LE deposited successfully.')
        else:
            print("Invalid input.")
    def Withdrawal(self,user_for_withdrawal):
        amount=int(input("Enter amount to be Withdrawn: "))
        if self.users_balances[self.users_usenames.index(user_for_withdrawal)]>amount:
            self.users_balances[self.users_usenames.index(user_for_withdrawal)]= self.users_balances[self.users_usenames.index(user_for_withdrawal)]-amount
            print(f'Processing...\n{amount} withdrawn successfully.')
        else:
            print("Insufficient balance.")
