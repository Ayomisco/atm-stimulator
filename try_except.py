username = ["ayo", 'ola']

enter_user = input("Enter username \n >> ")

try:
    userID = username.index(enter_user)

except:
    print(f"{enter_user} Does not exist in the list")