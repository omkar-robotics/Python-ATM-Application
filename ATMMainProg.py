from ATMMenu import menu
from ATMExcept import depositeError,withdrawError,inSuffFundError
from ATMOperation import deposite,withdraw,balenq
import sys
while(True):
  menu()
  try:
      ch=int(input("enter your choice :"))
      match(ch):
          case 1:
            try:
               deposite()
            except depositeError:
              print("dont enter -VE or zero for deposite value")
            except ValueError:
              print("your of operation should not be alumns,strs and symbol")
          case 2:
            try:
               withdraw()
            except withdrawError:
              print("dont enter -VE or zero for deposite value")
            except inSuffFundError:
              print("your acc does not have sufficient funds")
            except ValueError:
              print("your of operation should not be alumns,strs and symbol")
          case 3:
            balenq()
          case 4:
            print("thanks for using this programming")
            sys.exit()
          case _:
            print("your selection operation wrong try agin ")
  except ValueError:
    print("your of operation should not be alumns,strs and symbol")
    