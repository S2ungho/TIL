#Deposit(d) or withdrawal(w) or balance check(c)

def deposit(money):
    global balance
    balance = balance + money
    print(balance)

def withdrawal(money):
    global balance
    if balance > money:
        balance = balance - money
        print(balance)
    else:
        print("error : under "+ str(balance))

balance = 0
s = str(input("Deposit(d) or withdrawal(w) or balance check(c) or end(e): "))
while s != "e":
    if s == "d":
        money = int(input("deposit : "))
        deposit(money)
    elif s == "w":
        money = int(input("withdrawal : "))
        withdrawal(money)
    elif s == "c":
        print(balance)
    else:
        print("error")
    s = str(input("Deposit(d) or withdrawal(w) or balance check(c) or end(e): "))