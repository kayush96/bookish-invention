# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60
print("Welcome to Tip Calculator App\n")
total_amount = float(input("Enter your Total Bill Amount: "))
tip_percent = int(
    input("What percentange tip would you like to give? 10, 12 or 15? "))

total_people = int(input("How many people to split the bill? "))

split_amount = (total_amount/total_people) * (1 + (tip_percent/100))
total_tip = round(split_amount, 2)
total_tip = "{:.2f}".format(split_amount)
print(f"Each person should pay: ${total_tip}")
