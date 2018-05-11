a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in a:
    for j in b:
        print(i * j, end="")
    print("")

# 自己
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in a:
    for j in b:
        print(i, "x", j, "=", i * j, " ", end=" ")
    print("")

# 優
for i in range(1, 10):
    for j in range(1, 10):
        print("%d*%d=%2d" % (i, j, i * j), end=" ")
    print("")

# 變數輸入
a = int(input())
b = int(input())
for i in range(1, a):
    for j in range(1, b):
        print(i, "x", j, "=", i * j, " ", end=" ")
    print("")
