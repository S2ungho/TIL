def bank():
    global balance
    option=input("Deposit(d) or withdrawal(w) or balance check(c)??")
    if not option:  ##option==""
        return
    elif option=="w":
        withdraw()
    elif option=="d":
        deposit()
    elif option=="c":
        check()
    else:
        print("Please, press d or w or c or return")

def withdraw():
    global balance
    amount=int(input("How much?"))
    if balance-amount>=0:
        balance-=amount
        print("you've withdrawn {}won".format(balance))
    else:
       print("you can withdraw {}won".format(balance)) 

def deposit():
    global balance
    amount=int(input("How much?"))
    balance+=amount
    print("you deposited {}won".format(balance))


def check():
    print("your current balance is {}won".format(balance))

balance=0
bank()
