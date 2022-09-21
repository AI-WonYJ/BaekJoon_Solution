x = int(input())
y = int(input())
ma = x * y
if ma > 0:
    if x > 0:
        print(1)
    elif x < 0:
        print(3)
elif ma < 0 :
    if x > 0:
        print(4)
    elif x < 0:
        print(2)