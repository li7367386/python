# for迴圈
# range應用1+到100
sum = 0
for i in range(1, 101):  # 第三個參數調等差
    sum += i
    print(sum)

for x in range(3):  # range(1,4)
    x += 1  # 無
    for y in range(3):
        y += 1
        print("(" + str(x) + "," + str(y) + ")", end=" ")
    print()
