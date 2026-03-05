# encoding=GBK
# @Time : 2022/8/7 21:08
# @Author : YKW
# @File : stusystem.py
# 开始奇妙的python之旅吧！！！
import os

filename = 'student.txt'


def main():
    while True:
        menu()
        choice = int(input('请选择：\n'))
        if choice in [0, 1, 2, 3, 4, 5, 6, 7]:
            if choice == 0:
                ans = input('确定要推出系统吗？(y/n)')
                if ans in ['y', 'Y']:
                    print('谢谢你的使用!!!')
                    break
                else:
                    continue
            elif choice == 1:
                insert()  # 录入信息
            elif choice == 2:
                search()
            elif choice == 3:
                delete()
            elif choice == 4:
                modify()
            elif choice == 5:
                sort()
            elif choice == 6:
                total()
            elif choice == 7:
                show()


def menu():
    print('学生信息管理系统'.center(90, '='))
    print('功能菜单'.center(90, '-'))
    print('1.'.rjust(43), '录入学生信息')
    print('2.'.rjust(43), '查找学生信息')
    print('3.'.rjust(43), '删除学生信息')
    print('4.'.rjust(43), '修改学生信息')
    print('5.'.rjust(43), '排序学生信息')
    print('6.'.rjust(43), '统计学生总人数')
    print('7.'.rjust(43), '显示所有学生信息')
    print('0.'.rjust(43), '退出')
    print('-' * 90)


def insert():
    student_list = []
    while True:
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as rfile:
                student_old = rfile.readlines()
        id = input('请输入id(如1001):\t')
        if not id:  # 如果为空
            break
        with open(filename, 'r', encoding='utf-8') as wfile:
            flag = True
            for item in student_old:
                d = dict(eval(item))
                if d['id'] == id:
                    flag = False
                    print('找到学生信息了，可以修改!!!')
                    break
        if not flag:  # 存在，修改
            with open(filename, 'w', encoding='utf-8') as wfile:
                for item in student_old:
                    d = dict(eval(item))
                    if d['id'] == id:
                        while True:
                            try:
                                d['name'] = input("请输入姓名： ")
                                english = int(input('请输入英语成绩: '))
                                python = int(input('请输入Python成绩: '))
                                java = int(input('请输入Java成绩: '))
                            except:
                                print('您的输入有误，请重新输入！！！')
                            else:
                                break
                        wfile.write(str(d) + '\n')
                        print('修改成功！！！')
                    else:
                        wfile.write(str(d) + '\n')
        elif flag:  # 不存在， 追加
            name = input('请输入名字:\t')
            if not name:
                break
            try:
                english = int(input('请输入英语成绩: '))
                python = int(input('请输入Python成绩: '))
                java = int(input('请输入Java成绩: '))
            except:
                print('输入无效，不是整数类型，请重新输入！')
                continue
            # 将录入的学生信息保存到字典中
            student = {'id': id, 'name': name, 'english': english, 'python': python, 'java': java}
            # 将学生信息添加到列表中
            student_list.append(student)
            # 调用save()函数
            save(student_list)
            student_list.clear()
            print('学生信息录入完毕！！！')
        ans = input('是否继续添加？（y/n）\n')
        if ans == 'y':
            continue
        else:
            break


def save(lst):
    with open(filename, 'a', encoding='utf-8') as stu_txt:
        for item in lst:
            stu_txt.write(str(item) + '\n')


def search():
    student_query = []
    while True:
        id = ''
        name = ''
        if os.path.exists(filename):
            mode = input('按照ID查找请输入1，按姓名查找请输入2:')
            if mode == '1':
                id = input('请输入学生ID:')
            elif mode == '2':
                name = input('请输入学生姓名:')
            else:
                print('您的输入有误，请重新输入！！！')
                continue
            with open(filename, 'r', encoding='utf-8') as rfile:
                student = rfile.readlines()
                for item in student:
                    d = dict(eval(item))
                    if id != '':
                        if d['id'] == id:
                            student_query.append(d)
                    elif name != '':
                        if d['name'] == name:
                            student_query.append(d)

            # 显示查询结果
            show_student(student_query)
            # 清空列表
            student_query.clear()
            ans = input('是否要继续查询？（y/n）')
            if ans == 'y':
                continue
            else:
                break
        else:
            print('暂未保存学员信息')
            return


def show_student(lst):
    if len(lst) == 0:
        print('没有查询到学生信息，无数据显示！！！')
        return
    # 定义标题显示格式
    # 例子中format，用.format()中的参数替代前面的{}，{:^6}表示中间对齐，总占据6个宽度；其他有{:<6}表左对齐等
    format_title = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
    print(format_title.format('id', '姓名', '英语成绩', 'Python成绩', 'Java成绩', '总成绩'))
    # 定义内容显示格式
    format_data = '{:^6}\t{:^12}\t{:^8}\t{:^8}\t{:^8}\t{:^8}'
    for item in lst:
        print(format_data.format(item.get('id'),
                                 item.get('name'),
                                 item.get('english'),
                                 item.get('python'),
                                 item.get('java'),
                                 int(item.get('english')) + int(item.get('python')) + int(item.get('java'))

                                 ))


def delete():
    while True:
        student_id = input('请输入要删除的学生id:')
        if student_id != '':
            if os.path.exists(filename):
                with open(filename, 'r', encoding='utf-8') as file:
                    student_old = file.readlines()
            else:
                student_old = []
            flag = False
            if student_old:
                with open(filename, 'w', encoding='utf-8') as wfile:
                    d = {}
                    for item in student_old:
                        d = dict(eval(item))  # 将字符串转成字典
                        if d['id'] != student_id:
                            wfile.write(str(d) + '\n')
                        else:
                            flag = True
                    if flag:
                        print(f'id为{student_id}的学生信息已被删除')
                    else:
                        print(f'没有找到ID为{student_id}的学生信息')
            else:
                print('无学生信息')
                break
            show()  # 删除后显示所有学生信息
            ans = input('是否继续删除？（y/n）')
            if ans == 'y':
                continue
            else:
                break


def modify():
    show()
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            student_old = rfile.readlines()
    else:
        return
    student_id = input('请输入要修改的学员ID: ')
    with open(filename, 'w', encoding='utf-8') as wfile:
        flag = True
        for item in student_old:
            d = dict(eval(item))
            if d['id'] == student_id:
                flag = False
                print('找到学生信息了，可以修改!!!')
                while True:
                    try:
                        d['name'] = input("请输入姓名： ")
                        english = int(input('请输入英语成绩: '))
                        python = int(input('请输入Python成绩: '))
                        java = int(input('请输入Java成绩: '))
                    except:
                        print('您的输入有误，请重新输入！！！')
                    else:
                        break
                wfile.write(str(d) + '\n')
                print('修改成功！！！')
            else:
                wfile.write(str(d) + '\n')
        if flag:
            print('没有找到该id信息！请仔细核对！！！')
    ans = input('是否继续修改其他学生信息？（y/n）')
    if ans == 'y':
        modify()


def sort():
    show()
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            student_list = rfile.readlines()
        student_new = []
        for item in student_list:
            d = eval(item)
            student_new.append(d)
    else:
        return
    asc_or_dsc = input('请选择（0.升序 1.降序）:')
    if asc_or_dsc == '0':
        asc_or_dsc_bool = False
    elif asc_or_dsc == '1':
        asc_or_dsc_bool = True  # 降序
    else:
        print('您的输入有误，请重新输入！！！')
        sort()
    mode = int(input('请输入排序方式（1.按英语成绩，2.按Python成绩排序，3.按Java成绩排序，0.按总成绩排序'))
    if mode == 1:
        # lambda X：Y函数表示输入Y值，然后返回X值，实现返回字典中的key对应的value，再用sort进行排序，因为列表中的元素是字典，无法直接进行排序
        # x是代表student_new这个列表中的每个元素，这个列表是之前转换文件中的信息得到的，列表student_new中的元素是一个一个的字典
        # 相当于sort（）里面的key代表使用字典模式，把调用sort（）的对象里的字典放在第一个x里（x随便写什么），第二个x则是把第一个x里的字典给遍历了一下，并查询字典里的key（第二个x跟第一个必须一
        student_new.sort(key=lambda x: int(x['english']), reverse=asc_or_dsc_bool)
    elif mode == 1:
        student_new.sort(key=lambda x: int(x['python']), reverse=asc_or_dsc_bool)
    elif mode == 1:
        student_new.sort(key=lambda x: int(x['java']), reverse=asc_or_dsc_bool)
    elif mode == 0:
        student_new.sort(key=lambda x: (int(x['english']) + int(x['python']) + int(x['java'])), reverse=asc_or_dsc_bool)
    else:
        print('您的输入有误，请重新输入！！！')
        sort()
    show_student(student_new)


def total():
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            students = rfile.readlines()
            if students:
                print('一共有{}名学生。'.format(len(students)))
            else:
                print('还没有录入学生信息。')
    else:
        print('暂未保存数据信息！！！')


def show():
    student_list = []
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            students = rfile.readlines()
        for item in students:
            student_list.append(eval(item))
        if student_list:
            show_student(student_list)
    else:
        print('暂未保存数据信息！！！')


if __name__ == '__main__':
    main()
