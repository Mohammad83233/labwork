def power_of_two(lst):
    return list(map(lambda x: x**2, lst))
user_input = input("Enter a list of numbers separated by spaces: ")
my_list = list(map(int, user_input.split()))
result = power_of_two(my_list)
print("The power of 2 for each element:", result)

