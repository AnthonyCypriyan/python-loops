n = int(input())
count1 = 0
count2 = 0

while n > 0:
    digit = n % 10
    if digit % 2 == 0:
        count1 += 1
    else:
        count2 += 1
    n = n // 10

print("Even digits:", count1)
print("Odd digits:", count2)
