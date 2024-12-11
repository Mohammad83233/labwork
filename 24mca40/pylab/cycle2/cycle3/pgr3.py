
user_input = input("Enter numbers separated by spaces: ")
numbers = [int(num) for num in user_input.split()]
print(numbers)
total_sum = 0
for number in numbers:
    total_sum += number  
print("The sum of all items in the list is:", total_sum)
