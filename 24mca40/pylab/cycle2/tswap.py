string1=input("enter your string :")
string2=input("enter your string :")
swap_str1=string1[0]+string2[1]+string1[2:]
swap_str2=string2[0]+string1[1]+string2[2:]
string3=swap_str1+" "+swap_str2
print(string3)

