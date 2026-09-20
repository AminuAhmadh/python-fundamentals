# expense calculator
from statistics import mean

# welcome message
print("Hi, Welcome to Expense Calculator!\n")
print("------------------------------------")
print("------------------------------------\n")


# collecting input from user
total_items = int(input("How many total items? "))
items = {}
for item in range(total_items):
	entry = input("Enter item: ")
	price = int(input("Enter price: "))
	items[entry] = price


# print summary of expenses
print("Your expenses summary:")
print("------------------------------------\n")

print(f"You spent a total of: {sum(items.values())}")
print(f"Your average money spent is: {mean(items.values())}")
print(f"Your biggest purchase is {max(items, key=items.get)} for {max(items.values())}")