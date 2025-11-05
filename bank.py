balance = 0
def deposit(amount):
    global balance
    balance += amount
    print(f"Deposited ${amount}. New balance: ${balance}")
def withdraw(amount):
    global balance
    if amount <= balance:
        balance -= amount
        print(f"Withdrew ${amount}. New balance: ${balance}")
    else:
        print("Insufficient funds!")
def check_balance():
    print(f"Current balance: ${balance}")
