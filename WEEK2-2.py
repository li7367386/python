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

print(x, y, z, w, m, n)
