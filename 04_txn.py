# Transaction classifier: Amounts → small / medium / large.

print("Transaction classifier")
print("-------------------------")

print()

amount = int(input("What is the amount of your transaction? "))
if amount >= 10000:
    print("Your transaction is LARGE")
elif amount >= 1000:
    print("Your transaction is MEDIUM")
else:
    print("Your transaction is SMALL")