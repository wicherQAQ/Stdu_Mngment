import os

def menu():
    print('===============学生信息管理系统=================')
    print('==================功能菜单=====================')
    print('\t\t\t\t1.录入学生信息')
    print('\t\t\t\t2.查找学生信息')
    print('\t\t\t\t3.删除学生信息')
    print('\t\t\t\t4.修改学生信息')
    print('\t\t\t\t5.排序')
    print('\t\t\t\t6.统计学生总人数')
    print('\t\t\t\t7.显示所有学生信息')
    print('\t\t\t\t0.退出')
    print('==============================================')

# 将学生数据保存到磁盘
def save(student_list):
    try:
        filename = "student.txt"
        stu_txt = open(filename, 'a', encoding='utf-8')
    except:
        stu_txt = open(filename, 'w', encoding='utf-8')
    for item in student_list:
        stu_txt.write(str(item) + '\n')
    stu_txt.close()

def insert():
    student_list = []
    while True:
        id = input("请输入学生ID:")
        if not id:
            break
        name = input("请输入学生姓名:")
        if not name:
            break
        while True:
            try:
                sc_of_java = int(input("请输入Java成绩:"))
                sc_of_python = int(input("请输入Python成绩:"))
                sc_of_english = int(input("请输入English成绩:"))
                break
            except:
                print("输入无效，非整数类型，请重新输入！")
                continue

        stud = {'id': id, 'name': name, 'java': sc_of_java, 'python': sc_of_python, 'english': sc_of_english}
        student_list.append(stud)

        _exit = False
        while True:
            answer = input("是否继续添加y/n?")
            if answer is 'y':
                break
            elif answer is 'n':
                _exit = True
                break
            else:
                continue
        print(student_list)
        if _exit:
            break
    # 将数据保存到磁盘中
    save(student_list)

def search():
    while True:
        name = input("请输入要查找的学生姓名:")
        if not name:
            continue
        filename = "student.txt"
        isExist = os.path.exists(filename)
        if isExist:

            with open(filename, 'r', encoding='utf-8') as file:
                stud_list = file.readlines()
                obj = {}
                for item in stud_list:
                    obj = dict(eval(item))
                    if obj['name']==name:
                        print("ID" + '\t\t\t' + "姓名" + '\t\t\t' + "Java" + '\t\t' + "Python" + '\t\t' + "English")
                        str = "{}\t\t\t{}\t\t\t{}\t\t\t{}\t\t\t{}"
                        print(str.format(obj['id'],obj['name'],obj['java'],obj['python'],obj['english']))

        else:
            print("数据库中暂无该学生信息！")
        break

def delete():
    while True:
        id = input("请输入要删除的学生ID:")
        if not id:
            continue
        filename = "student.txt"
        if os.path.exists(filename):
            # 开始删除操作
            with open(filename, 'r', encoding='utf-8') as file:
                stud_list = file.readlines()
        else:
            stud_list = []

        if stud_list:
            answer = input("确认要删除吗y/n?")
            if answer == 'y':
                flag = False
                with open(filename, 'w', encoding='utf-8') as wfile:
                    d = {}
                    for item in stud_list:
                        d = dict(eval(item))
                        if d['id'] != id:
                            wfile.write(str(d) + '\n')
                        else:
                            flag = True
                    wfile.close()
                    if flag:
                        print(f"学生编号为{id}的学生已经删除", id)
                    else:
                        print(f"未找到学生编号为{id}的学生", id)
        else:
            print("无学生信息")

        answer = input("是否继续删除y/n?")
        if answer == 'y':
            continue
        if answer == 'n':
            break

def modify():
    while True:
        id = input("请输入要修改的学生ID:")
        if not id:
            continue
        filename = "student.txt"
        if os.path.exists(filename):
            # 开始删除操作
            with open(filename, 'r', encoding='utf-8') as file:
                stud_list = file.readlines()
        else:
            stud_list = []

        if stud_list:
            flag = False
            with open(filename, 'w', encoding='utf-8') as wfile:
                d = {}
                for item in stud_list:
                    d = dict(eval(item))
                    if d['id'] != id:
                        wfile.write(d + '\n')
                    else:
                        flag = True
                        # 开始修改
                        while True:
                            name = input("请输入学生姓名:")
                            if not name:
                                break
                            while True:
                                try:
                                    sc_of_java = int(input("请输入Java成绩:"))
                                    sc_of_python = int(input("请输入Python成绩:"))
                                    sc_of_english = int(input("请输入English成绩:"))
                                    break
                                except:
                                    print("输入无效，非整数类型，请重新输入！")
                                    continue
                            stud = {'id': id, 'name': name, 'java': sc_of_java, 'python': sc_of_python,
                                    'english': sc_of_english}
                            answer = input("确认要修改吗y/n?")
                            if answer == 'y':
                                wfile.write(str(stud) + '\n')
                                break
                            elif answer == 'n':
                                break
                wfile.close()
                if flag:
                    print(f"学生编号为{id}的学生已经修改完成", id)
                else:
                    print(f"未找到学生编号为{id}的学生", id)
        else:
            print("无学生信息")
        answer = input("是否继续修改y/n?")
        if answer == 'y':
            continue
        if answer == 'n':
            break


def sort():
    pass


def total():
    filename = "student.txt"
    if os.path.exists(filename):
        # 开始删除操作
        with open(filename, 'r', encoding='utf-8') as file:
            stud_list = file.readlines()
            print("学生的总人数：{}个".format(len(stud_list)))
            str1 = "学生的总人数：{}{}{}{}个"
            srt2=str1.format(12,34,34,34)
            print(srt2)

def show():
    filename = "student.txt"
    if os.path.exists(filename):
        # 开始删除操作
        with open(filename, 'r', encoding='utf-8') as file:
            stud_list = file.readlines()
            print("ID"+'\t\t\t'+"姓名"+'\t\t\t'+"Java"+'\t\t'+"Python"+'\t\t'+"English")
            for item in stud_list:
                stud = dict(eval(item))
                print(stud['id'] + '\t\t\t' + stud['name'] + '\t\t\t' + str(stud['java']) +'\t\t\t'+ str(stud['python'])
                + '\t\t\t' + str(stud['english']))





def main():
    while True:
        menu()
        inputNum = input("请输入：")
        if inputNum in ['0', '1', '2', '3', '4', '5', '6', '7']:
            if inputNum is '0':
                ansmer = input("你确定要退出系统吗？y/n?")
                if ansmer is 'y':
                    print("感谢使用，再见！")
                    break
            elif inputNum is '1':
                insert()
            elif inputNum is '2':
                search()
            elif inputNum is '3':
                delete()
            elif inputNum is '4':
                modify()
            elif inputNum is '5':
                sort()
            elif inputNum is '6':
                total()
            else:
                show()
        else:
            print("你输入的内容有误，请重新输入")

if __name__ == "__main__":
    main()
