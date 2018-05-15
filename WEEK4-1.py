# 利潤定價
# c = int(input("unit cost= "))
# r = int(input("unit retail price= "))
# N = int(input("base demand=  "))
# q = int(input("order amount= "))
c = int(input())
r = int(input())
N = int(input())
q = int(input())
P0 = float(input())
P1 = float(input())
P2 = float(input())
P3 = float(input())
P4 = float(input())
P5 = float(input())
P6 = float(input())
P7 = float(input())
P8 = float(input())

k = q * c
i = q * r
x = (0 - k)
y = (r - k)

if r < c:
    print("Error")
if q == 0:
    print("0 income")
if q == 1:
    profit1 = x * P0 + y * (1 - P0)
    print(int(profit1))
if q == 2:
    profit2 = x * P0 + y * P1 + (i - k) * (1 - (P0 + P1))
    print(int(profit2))
if q == 3:
    profit3 = x * P0 + y * P1 + (2 * r - k) * P2 + (i - k) * (1 - (P0 + P1 + P2))
    print(int(profit3))
if q == 4:
    profit4 = x * P0 + y * P1 + (2 * r - k) * P2 + (3 * r - k) * P3 + (i - k) * (1 - (P0 + P1 + P2 + P3))
    print(int(profit4))
if q == 5:
    profit5 = x * P0 + y * P1 + (2 * r - k) * P2 + (3 * r - k) * P3 + (4 * r - k) * P4 + (i - k) * (
            1 - (P0 + P1 + P2 + P3 + P4))
    print(int(profit5))
if q == 6:
    profit6 = x * P0 + y * P1 + (2 * r - k) * P2 + (3 * r - k) * P3 + (4 * r - k) * P4 + (5 * r - k) * P5 + (i - k) * (
            1 - (P0 + P1 + P2 + P3 + P4 + P5))
    print(int(profit6))
if q == 7:
    profit7 = x * P0 + y * P1 + (2 * r - k) * P2 + (3 * r - k) * P3 + (4 * r - k) * P4 + (5 * r - k) * P5 + (
            6 * r - k) * P6 + (i - k) * (1 - (P0 + P1 + P2 + P3 + P4 + P5 + P6))
    print(int(profit7))
if q == 8:
    profit8 = x * P0 + y * P1 + (2 * r - k) * P2 + (3 * r - k) * P3 + (4 * r - k) * P4 + (5 * r - k) * P5 + (
            6 * r - k) * P6 + (7 * r - k) * P7 + (i - k) * (1 - (P0 + P1 + P2 + P3 + P4 + P5 + P6 + P7))
    print(int(profit8))
