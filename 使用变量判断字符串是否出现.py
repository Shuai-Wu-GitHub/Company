# a = 0
computer = "hello"
user = input("请输入您要查找的字符串：")

for i in computer:
    if i == user:
        # a += 1
        # if a > 0 :
        print("找到了您输入的 ", i )
        break

else:
    print("没有找到您输入的数据")

