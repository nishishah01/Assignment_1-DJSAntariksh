#1. Billing 

total = 0.0
done = False

while not done:
    item = input("Enter item name (or 'done' to finish): ")

    if item.lower() == 'done':
        done = True
    else:
        price = input("Enter item price: ₹")

        # Check if price_input is a valid float
        if price.replace('.', '', 1).isdigit():  # Check if input is a valid number
            price = float(price) #converts the amount to float type
            total += price
        else:
            print("Invalid price entered. Please enter a valid number.")


print(f"Total amount to pay: ₹{total:}")


#2. Scorecard using dictionary

scores = {"Nishi": 85, "Jigisha": 72, "Raksha": 90, "Rashi": 88}
for student, score in scores.items():
    if score > 80:
        print(f"{student} scored {score}, which is above 80")
    elif score>60:
        print(f" {student} scored {score}, which is between 60 and 80")
    else:
        print(f" {student} scored {score}, which is below 60")
print("this was the result of sem 2")

#3. star print

rows =int(input("Enter the number of rows: "))
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()