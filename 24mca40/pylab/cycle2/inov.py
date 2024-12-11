integers=input("enter a list of integers seperated by commas :").split(',')
for i in range(len(integers)):
	if int(integers[i])>100:
		integers[i]='over'
print(integers)
