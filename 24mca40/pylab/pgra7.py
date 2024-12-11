def compare(S1, S2, n):
    
    if S1[:n] == S2[:n]:
        return True
    else:
        return False
S1 = input("Enter the first string (S1): ")
S2 = input("Enter the second string (S2): ")
n = int(input("Enter the number of characters to compare: "))
result = compare(S1, S2, n)
if result:
    print("The first", n, "characters of both strings are the same.")
else:
    print("The first", n, "characters of both strings are not the same.")
