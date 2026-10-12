from ATMExcept import depositeError,withdrawError,inSuffFundError
bal=500
def deposite():
    damt=int(input("enter your deposite amount :"))
    if (damt<=0):
        raise depositeError
    else:
        global bal
        bal=bal+damt
        print("your account xxxxxxxxx123 credited with INR:{}".format(damt))
        print("now account xxxxxxxxx123 bal INR:{}".format(bal))

def withdraw():
    global bal
    wamt=float(input("enter your withdraw account :"))
    if (wamt<=0):
        raise withdrawError
    elif(wamt>bal):
        raise inSuffFundError
    else:
        bal=bal-wamt
        print("your account xxxxxxxxx123 debited with INR:{}".format(wamt))
        print("now account xxxxxxxxx123 bal after withdraw INR:{}".format(bal))

def balenq():
    print("your bal in account xxxxxxxxxx123 INR:{}".format(bal))

