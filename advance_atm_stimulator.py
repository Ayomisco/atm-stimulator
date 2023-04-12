import time
import datetime

# Delay timing

# Welcome messages
print("Welcome to Otimum Global Bank")
print("... ")
time.sleep(3)

print("Please insert your card...")
print("...")
time.sleep(3)

allowed_users = ["ola", "ayo", "mayor", "olu"]
full_name = ["Ola Fola", "Ayo Francis", "Mayo Dami", "Olu Maintain"]
allowed_pin = [2222, 3333, 4444, 1111]
# Userbalance
ub = [34000, 34222, 34233, 34233]

naira = u"\u20A6"

general_trial = 9
trial = 3
username = input("Enter your username \n"
                                ">> ").lower()
while username in allowed_users:
    
    # if username not in allowed_users:
    #      print("User not found")
        try:
            while general_trial != 0:
                while trial != 0:
                    
                        userID = allowed_users.index(username)
                        print(userID)

                        confirm_password = input("Enter your pin")
                        if int(confirm_password) == userID[allowed_pin]:
                            print(f"Welcome {userID[full_name]}")
                            print(datetime.datetime.now)

                            
                        else:
                            print("Incorrect!")
        except:
            print("Try again")
# else:
#     print(f"{username} does not exist.")
#     continue



