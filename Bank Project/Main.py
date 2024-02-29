from BANK import Bank_Account

user_1= Bank_Account()

def menu1():
    options1 = """
                    Welcome to the bank.
                    =======================================
                    1- Login
                    2- Register
                    =======================================
                    """
    print(options1)
    
def menu2():
    options2 = """
                    select your operation.
                    =======================================
                    1- Check Balance
                    2- Deposit
                    3- Withdrawal
                    4- Exit
                    =======================================
                    """
    print(options2)

while True:
    menu1()
    user_input_1=(input())

    if user_input_1=='1':
        user_name_input= str(input("Enter Username: "))
        user_password_input= str(input("Enter Password: "))
        if user_1.login(user_name_input,user_password_input)=="ENTER":
            while True:
                menu2()
                user_input_2=(input())

                if user_input_2=='1':
                    user_1.check_balance(user_name_input)

                elif user_input_2=='2':
                    user_1.deposit(user_name_input)

                elif user_input_2=='3':
                    user_1.Withdrawal(user_name_input)

                elif user_input_2=='4':
                    break

                else:
                    print("Invalid input.")

    elif user_input_1=='2':
        user_1.registeration()

    else:
        print("Invalid input.")
