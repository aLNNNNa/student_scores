#学生管理系统
student=[]
def add_student():
    name=input("请输入学生姓名：")
    for s in student:
        if s["name"]==name:
            print("学生已存在！")
            return
    try:
        math=int(input("请输入数学成绩(0-100)："))
        chinese=int(input("请输入语文成绩(0-100)："))
        english=int(input("请输入英语成绩(0-100)："))
        if not (0 <= math <= 100 and 0 <= chinese <= 100 and 0 <= english <= 100):
            print("成绩必须在0到100之间！")
            return
    except ValueError:
        print("输入无效，请输入一个数字！")
        return
    student.append({"name":name,"math":math,"chinese":chinese,"english":english})
    print("添加成功！")
def view_students():
    if not student:
        print("没有学生信息，请先添加学生！")
        return
    print("\n学生信息列表：")
    for s in student:
        total=s["math"]+s["chinese"]+s["english"]
        print(f"姓名：{s['name']}，数学：{s['math']}，语文：{s['chinese']}，英语：{s['english'],}，总分：{total}")
def query_student():
    name=input("请输入要查询的学生姓名：")
    for s in student:
        if s["name"]==name:
            total=s["math"]+s["chinese"]+s["english"]
            avg=total/3
            print(f"姓名：{s['name']}，数学：{s['math']}，语文：{s['chinese']}，英语：{s['english']}，总分：{total}，平均分：{avg:.2f}")
            return
    print("未找到该学生信息！")
def statistics():
    if not student:
        print("没有学生信息，请先添加学生！")
        return
    n=len(student)
    math_scores=[s["math"] for s in student]
    chinese_scores=[s["chinese"] for s in student]
    english_scores=[s["english"] for s in student]
    print("\n成绩统计：")
    print(f"学生总数：{n}")
    print(f"数学 - 平均分：{sum(math_scores)/n:.2f}，最高分：{max(math_scores)}，最低分：{min(math_scores)}")
    print(f"语文 - 平均分：{sum(chinese_scores)/n:.2f}，最高分：{max(chinese_scores)}，最低分：{min(chinese_scores)}")
    print(f"英语 - 平均分：{sum(english_scores)/n:.2f}，最高分：{max(english_scores)}，最低分：{min(english_scores)}")
    #按总分排序
    def get_total(s):
        return s["math"]+s["chinese"]+s["english"]
    sortes_students=sorted(student,key=get_total,reverse=True)
    print("总分前三名：")
    for i,idx in enumerate(range(min(3,n))):
        s=sortes_students[i]
        total=get_total(s)
        print(f"{i+1}. 姓名：{s['name']}，总分：{total}")
def histogram():
    if not student:
        print("没有学生信息，请先添加学生！")
        return
    print("\n成绩分布图：")
    ranges=[(0,59),(60,69),(70,79),(80,89),(90,100)]
    labels=["0-59","60-69","70-79","80-89","90-100"]
    counts=[0]*len(ranges)#生成一个与ranges长度相同的列表，初始值为0
    for s in student:
        total=s["math"]+s["chinese"]+s["english"]
        avg=total/3
        for j,(low,high) in enumerate(ranges):
            if low <= avg <= high:
                counts[j] += 1#分别统计每个分数段的学生数量
                break
    for label,count in zip(labels,counts):#zip函数（把多个列表按相同下标打包配对）将labels和counts打包成一个元组列表，方便同时遍历标签和计数
        print(f"{label}: {count}人")#输出每个分数段的标签和对应的学生数量
while True:
    print("\n学生管理系统")
    print("1. 添加学生信息")
    print("2. 查看所有学生信息")
    print("3. 查询学生信息")
    print("4. 成绩统计")
    print("5. 成绩分布图")
    print("6. 退出系统")
    choice=input("请输入操作编号：")
    match choice:
        case "1":
            add_student()
        case "2":
            view_students()
        case"3":
            query_student()
        case "4":
            statistics()
        case "5":
            histogram()
        case "6":
            print("退出系统！")
            break
        case _:
            print("无效的操作编号，请重新输入！")
