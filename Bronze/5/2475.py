N = map(int, input().split())
sum = 0
for x in N:
    sum += x**2
print(sum % 10)