def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        result = 1
        for i in range(2, num + 1):
            result *= i
        return result
def sum_series(n):
    series_sum = 0
    for i in range(1, n + 1):
        term = (i ** i) / factorial(i)
        series_sum += term
    return series_sum
n = int(input("Enter the number of terms: "))
print(f"The sum of the series up to {n} terms is: {sum_series(n)}")
