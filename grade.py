# user input grade number and program outputs letter


num_grade = int(input("what is your grade: "))
if num_grade >= 70:
    print("Your grade is A.")
elif num_grade >= 60:
    print('Your grade is B.')
elif num_grade >= 50:
    print("Your grade is C.")
elif num_grade >= 45:
    print("your grade is D.")
elif num_grade >= 40:
    print("Your grade is E.")
else:
    print("Your grade is F. You are a failure. Atleast academically. Hopefully not in life also. cuz that will make you a pathetic loser")

