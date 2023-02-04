#Binary
l = []
n = int(input("Enter an integer"))
m = n
while m > 1:
    r = m%2
    m = m//2
    l.append(str(r))
l.reverse()
s = "".join(l)
result = str(m) + str(s)
print("Binary Form :- " , result)


#Decimal
n = int(input("Enter an integer"))
print("Decimal Form :- " , n)


#Octal
l = []
n = int(input("Enter an integer"))
m = n
while m > 7:
    r = m%8
    m = m//8
    l.append(str(r))
l.reverse()
s = "".join(l)
result = str(m) + str(s)
print("Octal Form :- " , result)


#Hexa
l = []
n = int(input("Enter an integer"))
m = n
while True:
    if m == 10:
        print("Hexa Form :- " , 'A')
        break
    if m == 11:
        print("Hexa Form :- " , 'B')
        break
    if m == 12:
        print("Hexa Form :- " , 'C')
        break
    if m == 13:
        print("Hexa Form :- " , 'D')
        break
    if m == 14:
        print("Hexa Form :- " , 'E')
        break
    if m == 15:
        print("Hexa Form :- " , 'F')
        break
    while m > 15:
        r = m%16
        if r == 10:
            r = 'A'
        if r == 11:
            r = 'B'
        if r == 12:
            r = 'C'
        if r == 13:
            r = 'D'
        if r == 14:
            r = 'E'
        if r == 15:
            r = 'F'
        m = m//16
        l.append(str(r))
    l.reverse()
    s = "".join(l)
    result = str(m) + str(s)
    print("Hexa Form :- " , result)
    break
