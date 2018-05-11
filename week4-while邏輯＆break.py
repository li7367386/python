# 判斷n的冪次
n = int(input())
k = 0
m = 1

while n > m:
    m *= 2
    k += 1
    print(m, k)

if m == n:
    print(n, "is 2 to the power of", k)

# 利用break判斷
n = int(input())
k = 0
m = n

while m > 1:
    if m % 2 != 0:
        break
    m //= 2
    k += 1
    print(m, k)
if m == 1:
    print(n, "is 2 to the power of", k)

# 解釋程式碼邏輯？
a = 1
b = 1
while a <= 10:
    while b <= 10:
        if b == 5:
            break
        print(a * b)
        b += 1
    a += 1
print(a)
