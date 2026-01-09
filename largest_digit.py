n = int(input())
maxi = 0
while n > 0:
    digit = n % 10
    if maxi < digit:
        maxi = digit
    n = n // 10
print(maxi)
