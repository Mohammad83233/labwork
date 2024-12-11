N=int(input("enter the value of N:"))
prime_number=[]
for num in range(2,N+1):
	prime=True
	for i in range(2,num):
		if num%i==0:
			prime=False
			break
	if prime:
		prime_number.append(num)
print(f"the alternative prime number till {N} are:")
for p in range(0,len(prime_number),2):
	print(prime_number[p])
