# prints out statistic of list of numbers based on users input

from statistics import mean, median, mode


num_list = list(int(input("Enter a number: ")) for i in range(5))
print("Mean", mean(num_list))
print("Median", median(num_list))
print("mode", mode(num_list))
print("Range", max(num_list)- min(num_list))

print("The numbers you entered are: ", num_list)
