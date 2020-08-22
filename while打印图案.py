a = 1
ou = 0
while a <= 100:
    if a % 2 == 0:
        ou+=a
    a+=1
print(ou)

a = 1

while a <= 5:
    b = 1
    while b <= 5 :
        print("*",end="")
        b += 1
    print("")
    a += 1
a = 1
while a <= 5:
    b = 1
    while b <= a :
        print("*",end="")
        b+=1
    a += 1
    print("")
