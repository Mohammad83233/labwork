lst1=[int(num) for num in input(" enter a list1(space seperated):").split()]
lst2=[int(num) for num in input(" enter a list2(space seperated):").split()]
length=len(lst1)==len(lst2)
lsum=sum(lst1)==sum(lst2)
common=set(lst1)&set(lst2)
if length:
	print("lists are the same")
else:
	print("the lists are not same")
print(f"lists common elements{common}")
if lsum:
	print(f"list sums are same")
else:
	print("the list sums are not same") 
