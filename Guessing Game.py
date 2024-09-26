

assigned_number = 25

while True:
    number = int(input("What is your number: "))
    
    if number > assigned_number:
        print("Little lower")
    elif number < assigned_number:
        print("Little higher")
    elif number == assigned_number:
        print("You won!")
        break