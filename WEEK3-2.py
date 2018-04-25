a = int(input())
b = int(1000 - a)
c = b % 500  # 214
d = c % 100  # 14
e = d % 50  # 14
f = e % 10  # 4
g = f % 5  # 4
h = g % 1  # 0

x = b // 500
y = c // 100
z = d // 50
w = e // 10
m = f // 5
n = g // 1

if x > 0:
    print("500,", str(x) + ";", end=" ")
if y > 0:
    print("100,", str(y) + ";", end=" ")
if z > 0:
    print("50,", str(z) + ";", end=" ")
if w > 0:
    print("10,", str(w) + ";", end=" ")
if m > 0:
    print("5,", str(m) + ";", end=" ")
if n > 0:
    print("1,", str(n), end=" ")
