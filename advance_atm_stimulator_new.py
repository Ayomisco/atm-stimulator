import time
import datetime

print("Welcome to Ayomide Bank")
print("... ")
time.sleep(3)

print("Please insert your card")
print("...")
time.sleep(3)


allowed_users = ["ola", "ayo", "mayor", "olu"]
full_name = ["Ola Fola", "Ayo Francis", "Mayo Dami", "Olu Maintain"]
allowed_pin = ["2222", "3333", "4444", "1111"]
# Userbalance
ub = [34000, 34222, 34233, 34233]

naira = u"\u20A6"

# Trials
g_trial = 9
trial = 3

# Main Starts
username = input("Enter your username \n"">> ").lower()
print("...")
time.sleep(3)

if username in allowed_users:
    while g_trial != 0:
        while trial != 0:

            user_id = allowed_users.index(username)

            confirm_pin = input("Enter your four digit pin \n" ">> ")
            if confirm_pin == allowed_pin[user_id]:

                full_name = full_name[user_id]
                print("...")
                time.sleep(2)
                print(f"Welcome {full_name}")
                print("==== ==== ==== ====")
                print(f"Current Time: {datetime.datetime.now()}")
                print("==== ==== ==== ====")

                # Transactions Begin
                transaction = input("Select transaction: \n"
                                    "1. Deposit \n"
                                    "2. Withdrawal \n"
                                    "3. Account Details \n"
                                    "4. Equiry"
                                    "5. Quit")



            else:
                print(f"Incorrect pin, Try again.")
                trial -= 1
                g_trial -= 1
                print(f"{trial} more trial left!")

                if g_trial == 0:
                    print(f"Your account as been locked. Please contact customer surpport.")
                    
                    quit()
                    

                if trial == 0:
                    print("Try again after 13 secs")
                    print("...")
                    trial = 3
                    time.sleep(1)
                  
                    continue
                # This below confirm the general trial
else:
    print(f"{username} not found!")
    print("Try again!")


