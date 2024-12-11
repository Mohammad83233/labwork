user_input = input("Enter a list of numbers separated by spaces: ")
numbers = list(map(int, user_input.split()))
multiples_of_3_only = list(filter(lambda x: x % 3 == 0, numbers))
print("Multiples of 3 in the list:")
for num in multiples_of_3_only:
    print(num)






