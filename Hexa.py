r = int(input("Enter range :- "))
for i in range(1 , r):
    l = []
    m = i
    n = i
    if i < r:
        if m == 10:
            print("Hexa Form :- " , 'A')
        if m == 11:
            print("Hexa Form :- " , 'B')
        if m == 12:
            print("Hexa Form :- " , 'C')
        if m == 13:
            print("Hexa Form :- " , 'D')
        if m == 14:
            print("Hexa Form :- " , 'E')
        if m == 15:
            print("Hexa Form :- " , 'F')
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
        if n < 10 or n > 15:
            l.reverse()
            s = "".join(l)
            result = str(m) + str(s)
            print("Hexa Form :- " , result)