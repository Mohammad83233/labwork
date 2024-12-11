even_digit_sqr=[]
for i in range(32,100):
	sqr=i*i
	if all(int(d)%2==0 for d in str(sqr)):
		even_digit_sqr.append(sqr)
print("the four digit number are:",even_digit_sqr)
