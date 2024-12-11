upper_limit=int(input("'enter the number for limit :"))
total_sum=0
for number in range(1,upper_limit):
	if number%6==0 and number%4==0:
		print(number)
		total_sum+=number
print(f"the sum of all integer below {upper_limit} that are divisible by 6 but not by 4 is:{total_sum}")

