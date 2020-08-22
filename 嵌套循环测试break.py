a = 1
while a <= 3:
    print("这是第%d次循环" % a)
    b = 1
    while b <= 3:
        print("这是第%d次内循环" % b)
        if b == 2:
            break
        b += 1
    a += 1