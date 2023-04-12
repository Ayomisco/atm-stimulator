import time

print("Welcome to Ayomide Bank")
time.sleep(2)

username = "ayomide"
pin = 2343
available_balance = 40000

print("Insert your card")
print("**** **** ****")

pin_entry = input("Please enter your pin \n" ">>> ")

if pin == int(pin_entry):
    print("Welcome", username)

    transaction = input("Select transaction: \n"
                        "1. Deposit \n"
                        "2. Withdrawal \n"
                        "3. Check Balance \n"
                        "4. Logout \n"
                        ">>> ")
    print("**** **** ****")
    time.sleep(2)

    if transaction.lower() == "deposit" or transaction == "1":
        deposit_amount = input("Enter amount to be deposited \n")

        total = int(deposit_amount) + int(available_balance)
        print(f"You have successfully added {deposit_amount} to your existing balance.")
        print(f"Therefore, your total balance is {total}")
        print("**** **** ****")
        print("Thank you for banking with us")
    
   
    elif transaction.lower() == "c" or transaction == "3":
        print(f"Your current balance is {available_balance}")
        print("**** **** ****")
        print("Thank you for banking with us ")
    
    else:
        print("**** **** ****")
        print("Thank you for banking with us ")
        exit()


else:
    print("Incorrect pin! Try again later.")
