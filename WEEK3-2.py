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
    fivehundreds = "500, " + str(x) + "; "
else:
    fivehundreds = ""
if y > 0:
    onehundred = "100, " + str(y) + "; "
else:
    onehundred = ""
if z > 0:
    fifty = "50, " + str(z) + "; "
else:
    fifty = ""
if w > 0:
    ten = "10, " + str(w) + "; "
else:
    ten = ""
if m > 0:
    five = "5, " + str(m) + "; "
else:
    five = ""
if n > 0:
    one = "1, " + str(n)
else:
    one = ""

# print(fivehundreds + onehundred + fifty + ten + five + one)

k = (fivehundreds + onehundred + fifty + ten + five + one)

if k[-2] == ";":
    k = k[:-2]
    print(k)
else:
    print(k)