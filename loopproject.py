pin=1234
balance=1000
attempts=0
while attempts<3:
    enter_pin=int(input("Please enter your pin : "))
    if enter_pin!=pin:
        attempts += 1
        print(f"Pin incorrect, you have {3-attempts} left")
    if enter_pin==pin:
        print("Successfully login")
    while True:
        print("\n----ATM Menu----")
        print("1.Check Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4. Exit")

        choice=int(input("Please enter the choice : "))
        if choice==1:
            print(f"You balance amount is {balance}")
        elif choice==2:
            amount=int(input("Enter the amount to deposit"))
            amount=balance+amount
            print(f"{amount} deposited to account")
        elif choice==3:
            withdraw_amt=int(input("Enter the amount to withdraw"))
            if withdraw_amt>amount:
                print("Insufficient balance")
                continue
            balance=balance-amount
            print(f"{withdraw_amt} withdrawed from account")
        elif choice==4:
            print("Successfully Logged out")
        else:
            print("Please select a valid input")
        break




