x1 = int(input())
x2 = int(input())
y = int(input())
if y <= x1:
    account1 = x1 - y
    account2 = x2 + y
else:
    account1 = x1 - x1
    account2 = x2 + x1
print(account1, account2)

# x1 = int(input())
# x2 = int(input())
# y = int(input())
# if y <= x1:
#     account = (x1 - y, x2 + y)
# else:
#     account = (x1 - x1, x2 + x1)
# print(account)
