def CheckBalance(cash):
    print(cash)
    
def WithdrawCash(cash):
    amount = int(input())
    cash -= amount
    return cash
    
def DepositCash(cash):
    amount = int(input())
    cash += amount
    return cash

pin_default = "1010"
cash = 5000

pin = input()
if pin != pin_default:
    quit()

done = False

while not done:
    
    choice = int(input())
    
    if choice == 1:
        CheckBalance(cash)
    
    elif choice == 2:
        cash = WithdrawCash(cash)
        print(cash)
        
    elif choice == 3:
        cash = DepositCash(cash)
        print(cash)
        
    elif choice == 4:
        print("Thanks for the Transaction")
        done = True