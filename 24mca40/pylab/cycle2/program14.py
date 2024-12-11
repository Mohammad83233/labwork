numbers=[-12,15,-7,8,-30,180,0]
pos=[num for num in numbers if num>0]
print(f"positive numbers in {numbers}:",pos)
N=7
sqr=[num**2 for num in range(1,N+1)]
print("squares of first 7 numbers:",sqr)
word="shinepaul"
vowels=[char for char in word if char in 'aeiouAEIOU']
print(f"vowels in the word:{word}",vowels)
word="cycle"
ordinal_values=[ord(char) for char in word]
print("ordinal values of each character in the word:cycle",ordinal_values)

