names = input("Enter names separated by commas: ").split(',')
names = [name.strip() for name in names]
print("Stored list of names:", names)
count_a = sum(name.strip().lower().count('a') for name in names)
print(f"The letter 'a' appears {count_a} times in the list of names.")

