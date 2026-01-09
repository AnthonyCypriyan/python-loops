n = int(input())
l = [0,0,0,0,0,0,0,0,0,0]

while n > 0:
    digit = n % 10
    l[digit] += 1
    n = n // 10

for i in range(10):
    if l[i] > 0:
        print(i, "->", l[i])
