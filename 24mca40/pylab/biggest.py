n1=int(input("enter your first number :"))
n2=int(input("enter your second number :"))
n3=int(input("enter your third number :"))
if n1>n2 and n1>n3:
	print(f"{n1} is the biggest")
elif n2>n3 and n2>n1:
	print(f"{n2} is the biggest")
else:
	print(f"{n3} is the biggest")

