string=input("enter a string :")
first_char=string[0]
new_string=first_char+string[1:].replace(first_char,"$")
print("modified string:",new_string)

