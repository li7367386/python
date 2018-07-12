# # 字串切割成清單
gradeStr = input()  # 1,2,3,4,5
grades = gradeStr.split()  # split(',')
print(grades)

gradeStr = input()
grades = gradeStr.split()
print(grades[0], grades[2] * 2)  # 取位置 可運算
print(len(grades))  # 長度

gradeStr = input()
grades = gradeStr.split()
grades.append([9, 7, 5])  # append()list最後面加上item
print(grades)  # ['1', '2', '3', [9, 7, 5]]
print(grades[3][1])  # [9,7,5]的7
print(grades[3][0] + grades[3][1] + grades[3][2])  # 9+7+5=21

# 把字串改成整數(1)
gradeStr = input()
gradelist = gradeStr.split()
print(gradelist)
grades = []

for g in gradelist:
    grades.append(int(g))
print(grades)

# 字串改整數＋運算(2)
gradeStr = input()
grades = gradeStr.split()
print(grades)

for i in range(len(grades)):
    grades[i] = int(grades[i]) * 2
print(grades)
