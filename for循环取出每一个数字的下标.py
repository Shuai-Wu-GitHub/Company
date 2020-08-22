str = "hello"
index = 0
for i in str:
    print(i)

while index < len(str):
    value = str[index]
    index += 1
    print(value)


for i in range(5):
    print("* ")