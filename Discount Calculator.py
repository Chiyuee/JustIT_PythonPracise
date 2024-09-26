total = float(input("What is your total shopping amount?"))

if total >= 100:
    new_total = total - ((total / 10) * 2)
    print(f"You are eligible to apply a 20% discount, making your total ${new_total}")
elif total >= 50:
    new_total = total - (total / 10)
    print(f"You are eligible to apply a 10% discount, making your total ${new_total}")
else:
    print(f"Your total cost is {total}")