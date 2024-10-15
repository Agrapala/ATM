import time
import sys

user_balance = 10000

print("Welcome to ABC Bank $$ ")
time.sleep(1)

attempts= True
while attempts == True :
    attempt1 = int(input("Enter Your PIN CODE: "))
    if attempt1 == 9505 :
        print("PIN is corrected")
        time.sleep(1)
        
        menu = int(input("""
        Please Select Your Opinion
        1.Check Balance
        2.Cash Withdraws
        3.Cash Deposites
        """))
        if menu == 1 :
            print(f"Your Account Balance: {user_balance}")
            
            time.sleep(0.25)
        
        elif menu == 2 :
            print("Choose your withdraw amount: ")
            time.sleep(0.75)
            withdraw=int(input(""" 
                            1.500
                            2.1000
                            3.2000
                            4.4600
                            5.other amount 
                                
                               """))

            if withdraw == 1:
                if user_balance>500 :
                    print(f"Success.Your account balance is {user_balance - 500}")
                
                else :
                    print("Insufficiant account balance.")
                

            elif withdraw == 2:
                if user_balance>1000 :
                    print(f"Success.Your account balance is {user_balance - 1000}")
                
                else :
                    print("Insufficiant account balance.")
                
            elif withdraw == 3:
                    if user_balance>2000 :
                        print(f"Success.Your account balance is {user_balance - 2000}")
                    
                    else :
                        print("Insufficiant account balance.")
                        
            elif withdraw == 4:
                    if user_balance>4600 :
                        print(f"Success.Your account balance is {user_balance - 4600}")
                        
                    else :
                        print("Insufficiant account balance.")
                        
            elif withdraw == 5:
                    give_amount=int(input("Enter Amoount: "))
                    if user_balance>give_amount:
                        print(f"Success.Your account balance is {user_balance - give_amount}")
                        
                    else :
                        print("Insufficiant account balance.")
        elif menu ==3 :
            depo = int(input("ADD MONEY : "))   
            user_balance = user_balance + depo    
            print(f"Your Account Balance is :{user_balance}")  
             

    else :
        print("Incorrected PIN")
        attempt2 = int(input("Enter Your PIN CODE: "))
        if attempt2 == 9505 :
            print("PIN is corrected")
            continue
        else:
            print("Try Next Time !!")
            break

        
