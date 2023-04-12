import time
import datetime


allowed_users = ["ola", "ayo", "mayor", "olu"]
full_name = ["Ola Fola", "Ayo Francis", "Mayo Dami", "Olu Maintain"]
allowed_pin = ["2222", "3333", "4444", "1111"]
# Userbalance
acct_balance = [34000, 34222, 34233, 34233]

print("Welcome to Sam Bank...")
print("...")
time.sleep(2)

print("Insert your card")
print("...")
time.sleep(2)
general_trial = 9
main_trial = 3

username = input("Enter your name \n" 
                 ">> ")

if username in allowed_users:



    while general_trial != 0:
        while main_trial != 0:
            userid = allowed_users.index(username)

            pin = input("Enter your four digit pin \n"
                        ">> ")
            
            
            if pin == allowed_pin[userid]:
                full_name = full_name[userid]
                print(f"Welcome {full_name}")

                print("====== ===== ======")
                current_time_date = datetime.datetime.now()
                print(current_time_date)
                print("====== ===== ======")
            

            else:
                print("Incorrect pin")
                general_trial -= 1
                main_trial -= 1
                print(f"{main_trial} more trial left...")

                # Confirming if the general trial and main trial
                if general_trial == 0:
                    print("Card block!!!")
                    print("Contact our customer service")
                    exit()

                if main_trial == 0:
                    print("Card locked!!! Try again after 3 minute.")
                    time.sleep(4)
                    main_trial = 3
                    continue




else:
    print(f"{username} does not exist. Try again!")


