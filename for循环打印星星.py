for i in range(5):
    for i in range(5):
        print("* " , end = "")
    print("")

print("==================================")

a = 1
for i in range(5):
    for i in range(a):
        print("* " , end = "")
    a += 1
    print("")