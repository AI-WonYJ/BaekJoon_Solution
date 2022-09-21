while True:
    A, B = input().split()
    if A == '0' and B == '0':
        break
    sum = int(A) + int(B)
    print(sum)