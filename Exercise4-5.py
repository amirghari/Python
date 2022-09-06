input_username = input("Enter your username")
input_password = input("Enter your password")
username = "python"
password = "rules"
attempts = 0
if username == input_username and password == input_password:
    print("welcome")
else:
    while (username != input_username or password != input_password) and attempts < 4:
        print("Please try again")
        input_username = input("Enter your username")
        input_password = input("Enter your password")
        attempts += 1
    if username == input_username and password == input_password:
        print("welcome")
    else:
        print("access denied")
