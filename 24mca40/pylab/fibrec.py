def fibonacci(n):
	if n<=1:
		return n
	else:
		return fibonacci(n-1)+fibonacci(n-2)
num_terms=int(input("enter the number of terms :"))
if num_terms<=0:
	print("please enter a positive integer")
else:
	print("fibonacci sequence:")
	for i in range(num_terms):
		print(fibonacci(i))
