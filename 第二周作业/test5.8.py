user_list = ["wang", "yang", "fang"]

for user in user_list:
    if user == "admin":
        print("Hello %s, would you like to see a status report?"%user)
    else:
        print(f"Hello {user}, thank you for logging in again")