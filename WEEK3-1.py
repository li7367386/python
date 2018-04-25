x1 = int(input())
x2 = int(input())
y = int(input())
if y <= x1:
    account1 = x1 - y
    account2 = x2 + y
else:  # else better
    account1 = x1 - x1
    account2 = x2 + x1
print(account1, account2)
