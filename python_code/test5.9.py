user_list = ["wang", "yang", "hu"]

if user_list:
    for user in user_list:
        if user == "wang":
            print("Hello %s, would you like to see a status report?"%user)
        else:
            print(f"Hello {user}, thank you for logging in again")
else:
    print("We need to find some users!")


user_list = []

if user_list:
    for user in user_list:
        if user == "wang":
            print("Hello %s, would you like to see a status report?"%user)
        else:
            print(f"Hello {user}, thank you for logging in again")
else:
    print("We need to find some users!")