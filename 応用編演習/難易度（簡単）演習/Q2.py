students=[
    ["田中",85],
    ["佐藤",72],
    ["鈴木",91],
    ["中村",54]
]
#生徒名表示
print(students)

#平均点
total=0
for student in students:
    total=total+student[1]
print(f"平均点:{total/len(students)}")

#合格者集計
for student in students:
    if student[1]>=60:
        print(f"合格:{student[0]}")
    else:
        print(f"不合格:{student[0]}")

#最高点
highest=students[0]
for student in students:
    if student[1]>highest[1]:
        highest=student
print(f"最高点:{highest}")
