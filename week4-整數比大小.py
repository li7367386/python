# 三個整數比大小，找最小
a = int(input())
b = int(input())
c = int(input())


if a <= b:
    if a <= c:
        print(a, "is the smallest")
    else:
        print(c, "is the smallest")
else:
    if b <= c:
        print(b, "is the smallest")
    else:
        print(c, "is the smallest")

# 優化
min = 0
if a <= b:
    if a <= c:
        min = a
    else:
        min = c
else:
    if b <= c:
        min = b
    else:
        min = c
print(min)

# 再優化
min = c
if a <= b:
    if a <= c:
        min = a
    else:
        min = c
else:
    if b <= c:
        min = b
    else:
        min = c
print(min, "is the smallest")

# 精簡
if a <= b:
    min = a if (a <= c) else c
else:
    min = b if (b <= c) else c
print(min)

# 精簡+邏輯輔助()
if a <= b:
    min = (a if (a <= c) else c)
else:
    min = (b if (b <= c) else c)

print(min)