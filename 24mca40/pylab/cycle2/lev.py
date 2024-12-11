lst=[int(num) for num in input("enter a list of numbers(space seperated):").split()]
odd_lst=[odd for odd in lst if odd%2!=0]
print(odd_lst)

