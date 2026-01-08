n = int(input())
rev = 0
s = n
while n > 0:
    rev = rev * 10 + n % 10
    n //= 10

if rev == s:
    print("Palindrome")
else:
    print("Not Palindrome")
