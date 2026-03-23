# This is a mini bank simulation game or system.

def check_balance(balance):
    print("your current balance is:",balance)
    return balance

def deposite_money(amount1,balance):
    balance += amount1
    print(f"{amount} succesfully deposited")
    return balance

def withdraw_money(balance,amount1):
    if amount>balance:
        print("insufficient balance.")
    else:
        balance-=amount1
        print(f" withdraw {amount} successfully")
        return balance
    
balance=1000
def main():
    print("\n----ATM Menu-----")
    print("1. check Balance.")
    print("2. Deposite money.")
    print("3. Withdraw Money.")
    print("4. Exit.")
main()
choice=int(input("enter your choice (1-4):"))

if choice==1:
    check_balance(balance)

elif choice==2:
    amount=int(input("Enter the amount:"))
    deposite_money(balance,amount)

elif choice==3:
   amount=int(input("Enter the amount:"))
   withdraw_money(balance,amount)

elif choice==4:
    print("Thank you for using our ATM service.")
    exit()

else :
    print("invalid  choice. Try again")
