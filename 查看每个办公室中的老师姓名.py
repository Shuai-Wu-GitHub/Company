import random
'''
将所有老师随机分配到三个办公室中，并输出第几个办公室中有几个人，输出老师的姓名

思路：遍历所有的老师，随机生成数1,2,3表示办公室，将老师添加进办公室中

遍历办公室列表，获取每一个办公室,打印出每一个老师的姓名
'''

office_list = [[],[],[]]
teacher_list = ["A老师","B老师","C老师","D老师","E老师","F老师","G老师","H老师"]

for teacher in teacher_list:
    office_num = random.randint(0,2)
    # print(office_num)
    office_list[office_num].append(teacher)
    # print(teacher_name)
print(office_list)


a = 1
for office in office_list:
    num = len(office)
    print("第%d个办公室有%d人" % (a,num))
    for i in office:
        print(i)
    a += 1
