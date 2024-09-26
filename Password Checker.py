predefined_password = "password123"


attempts = 3
while True:
    if attempts == 0:
        print("Access denied.")
        break
    user_password = input("What is your password: ")
    
    if predefined_password == user_password:
        print("Access granted")
        break
    else:
        attempts -= 1
        print(f"Wrong password. You have {attempts} attempt(s) left")
