a, CC = map(str, input("Первое слагаемое, СС ").split())
CC = int(CC)
sl1 = int(a, CC)

a, CC = map(str, input("Второе слагаемое, СС ").split())
CC = int(CC)
sl2 = int(a, CC)

CC = int(input("А выводить в СС "))

a = sl1 + sl2

if CC == 2:
    an = bin(a)
    print(an, end="")


elif CC == 8:
    an = oct(a)
    print(an, end="")


elif CC < 10:
    an = ''
    while a > 0:
        an = str(a % CC) + an
        a = a // CC
    print(an, end="")

elif CC == 16:
    an = hex(a)
    print(an, end="")

else:
    clon_a = a
    count_yach = 0
    while a > CC:
        a //= CC
        count_yach += 1
    an = [None] * (count_yach + 1)
    a = clon_a
    for i in range(count_yach, -1, -1):
        if i == 0:
            if a == 10:
                an[i] = "A"
            elif a == 11:
                an[i] = "B"
            elif a == 12:
                an[i] = "C"
            elif a == 13:
                an[i] = "D"
            elif a == 14:
                an[i] = "E"
            elif a == 15:
                an[i] = "F"
        else:
            if a % CC == 10:
                an[i] = "A"
            elif a % CC == 11:
                an[i] = "B"
            elif a % CC == 12:
                an[i] = "C"
            elif a % CC == 13:
                an[i] = "D"
            elif a % CC == 14:
                an[i] = "E"
            elif a % CC == 15:
                an[i] = "F"
            else:
                an[i] = a % CC
        a //= CC
    print(*an, end="")
input()
